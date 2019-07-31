from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length = 200)
    description = models.TextField(null = True)
    price = models.IntegerField()
    image = models.ImageField(upload_to = "images/", null = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    # ForeignKey: Post마다 username이 있음
    # CASCADE: User가 삭제되면 그 유저의 Post도 모두 삭제 cf. PROTECT, SET_NULL
    
    creared_at = models.DateTimeField(auto_now_add = True)
    uploaded_at = models.DateTimeField(auto_now = True)