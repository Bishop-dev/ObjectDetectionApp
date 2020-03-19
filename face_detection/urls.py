from django.urls import path

from . import views

app_name = 'face_detection'
urlpatterns = [
    path('', views.index, name='index')
]
