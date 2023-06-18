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

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Emotion_Detection.h5')
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
            cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, 'No Face Found', (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    # Return the processed frame and emotion list
    return frame, emotion_list


@csrf_exempt
def capture_and_detect_emotion(request):
    if request.method == 'POST':
        # Get the image data from the request
        image_data = request.POST.get('image_data', None)
        if image_data:
            # Decode the image data and save it as a temporary file
            binary = b64decode(image_data.split(',')[1])
            with open('temp.jpg', 'wb') as f:
                f.write(binary)
            # Read the image from the temporary file
            frame = cv2.imread('temp.jpg')
            # Process the image and detect emotions
            processed_frame, emotion_list = detect_emotion(frame)
            # Delete the temporary file
            os.remove('temp.jpg')
            # Return the processed image or emotion data as desired
            return JsonResponse({'emotion_list': emotion_list})
    return JsonResponse({'error': 'Invalid request'})

@csrf_exempt
def my_view(request):
    # Render the template with a form or any other way to capture an image
    return render(request, 'my_template.html')
