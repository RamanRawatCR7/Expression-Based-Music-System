from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from base64 import b64decode
from PIL import Image
from keras.models import load_model
from tensorflow.keras.utils import img_to_array
import cv2
import numpy as np
import os
from statistics import mode
import webbrowser
import random

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
model_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'Emotion_Detection.h5')
classifier = load_model(model_path)
class_labels = ['Angry', 'Happy', 'Neutral', 'Sad', 'Surprise']


@csrf_exempt
def detect_emotion(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    emotion_list = []
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
        if np.sum([roi_gray]) != 0:
            roi = roi_gray.astype('float') / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)
            preds = classifier.predict(roi)[0]
            label = class_labels[preds.argmax()]
            emotion_list.append(label)
            label_position = (x, y)
            cv2.putText(frame, label, label_position,
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, 'No Face Found', (20, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
    varRes = mode(emotion_list)
    neutral = ['https://www.youtube.com/watch?v=5mFTXbZzOAE', 'https://www.youtube.com/watch?v=k5VUKozfNsc',
               'https://www.youtube.com/watch?v=_ae2j9jZY_U', 'https://www.youtube.com/watch?v=xCatIOFua2E']
    happy = ['https://www.youtube.com/watch?v=AYcxiROIktI&ab_channel=T-Series', 'https://www.youtube.com/watch?v=ZbZSe6N_BXs&ab_channel=PharrellWilliamsVEVO', 'https://www.youtube.com/watch?v=ipii7KbbJLY&ab_channel=PopularMusic', 'https://www.youtube.com/watch?v=iPUmE-tne5U&ab_channel=KatrinaTheWavesVEVO',
             'https://www.youtube.com/watch?v=ru0K8uYEZWw&ab_channel=justintimberlakeVEVO', 'https://www.youtube.com/watch?v=09R8_2nJtjg&ab_channel=Maroon5VEVO',
             'https://www.youtube.com/watch?v=d-diB65scQU&ab_channel=BobbyMcFerrinVEVO', 'https://www.youtube.com/watch?v=6POZlJAZsok&ab_channel=GroverWashington%2CJr.-Topic', 'https://www.youtube.com/watch?v=HNBCVM4KbUM&ab_channel=BobMarleyVEVO']
    sad = ['https://www.youtube.com/watch?v=HiXx5JFRxb4', 'https://www.youtube.com/watch?v=cyEvAHP8_60', 'https://www.youtube.com/watch?v=YwgNpObouB0'
           'https://www.youtube.com/watch?v=xrcMgO2fgpA', 'https://www.youtube.com/watch?v=JNKjudIKkLg',
           'https://youtu.be/DQ4r7HegRQw']
    surprise = ['https://www.youtube.com/watch?v=ZbZSe6N_BXs&ab_channel=PharrellWilliamsVEVO', 'https://www.youtube.com/watch?v=21LGv8Cf0us&ab_channel=SCEntertainment', 'https://www.youtube.com/watch?v=ipii7KbbJLY&ab_channel=PopularMusic', 'https://www.youtube.com/watch?v=qK5KhQG06xU&ab_channel=Audioandlyrics',
                'https://www.youtube.com/watch?v=eYSbUOoq4Vg&ab_channel=pluisje666', 'https://www.youtube.com/watch?v=1We3b8V45Rg&ab_channel=Uknow', 'https://www.youtube.com/watch?v=ApXoWvfEYVU&ab_channel=PostMaloneVEVO', 'https://www.youtube.com/watch?v=mRD0-GxqHVo&ab_channel=GlassAnimalsVEVO', 'https://www.youtube.com/watch?v=jJPMnTXl63E&ab_channel=PowfuVEVO',
                'https://www.youtube.com/watch?v=kTJczUoc26U&ab_channel=TheKidLAROIVEVO']
    angry = ['https://www.youtube.com/watch?v=ETNRfcNIl2w&ab_channel=SofieSo', 'https://www.youtube.com/watch?v=mQvteoFiMlg&ab_channel=EminemVEVO', 'https://www.youtube.com/watch?v=S9bCLPwzSC0&ab_channel=EminemVEVO', 'https://www.youtube.com/watch?v=ndCI8DIM86w&list=RDGMEMHDXYb1_DDSgDsobPsOFxpA&start_radio=1&rv=xuhl6Ji5zHM&ab_channel=XXXTENTACION-Topic',
             'https://www.youtube.com/watch?v=P9L_ZWVPX4g&list=RDGMEMHDXYb1_DDSgDsobPsOFxpA&index=4&ab_channel=TrevorDaniel-Topic']
    if varRes == 'Neutral':
        webbrowser.open(random.choice(neutral))
    if varRes == 'Happy':
        webbrowser.open(random.choice(happy))
    if varRes == 'Sad':
        webbrowser.open(random.choice(sad))
    if varRes == 'Surprise':
        webbrowser.open(random.choice(surprise))
    if varRes == 'Angry':
        webbrowser.open(random.choice(angry))
    return frame, emotion_list


@csrf_exempt
def capture_and_detect_emotion(request):
    if request.method == 'POST':
        image_data = request.POST.get('image_data', None)
        if image_data:
            binary = b64decode(image_data.split(',')[1])
            with open('temp.jpg', 'wb') as f:
                f.write(binary)
            frame = cv2.imread('temp.jpg')
            processed_frame, emotion_list = detect_emotion(frame)
            os.remove('temp.jpg')
            return JsonResponse({'emotion_list': emotion_list})
    return JsonResponse({'error': 'Invalid request'})


@csrf_exempt
def my_view(request):
    return render(request, 'my_template.html')
