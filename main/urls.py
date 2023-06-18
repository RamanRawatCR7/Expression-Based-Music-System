from django.urls import path
from main.views import my_view, capture_and_detect_emotion

app_name = 'main'

urlpatterns = [
    path('', my_view, name='my_view'),
    path('capture/', capture_and_detect_emotion, name='capture_and_detect_emotion'),
]
