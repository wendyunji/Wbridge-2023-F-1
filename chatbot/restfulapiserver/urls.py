from django.conf.urls import url, include
from addresses import views
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('addresses/', views.address_list),
    path('addresses/<int:pk>/', views.address),
    path('login/', views.login),
    path('app_login/', views.app_login),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('chat_service/', views.chat_service, name='chat_service'),
    path('chat_service/image_upload/', views.image_upload),
    path('', views.main)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)