from django.db import models
# Create your models here.


class Addresses(models.Model):
    name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=13)
    address = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


class Image(models.Model):
    imgfile = models.ImageField(null=True, upload_to="", blank=True) # 이미지 컬럼 추가