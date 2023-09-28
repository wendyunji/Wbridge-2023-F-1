from django.urls import path

from . import views


urlpatterns = [
    path('', views.chat_service, name='chat_service'),
    path('/image_upload/', views.image_upload, name='image_upload'),
]