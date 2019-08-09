from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blogger(models.Model):
    blogger = models.OneToOneField(User, on_delete=models.CASCADE)
    post_code = models.IntegerField()
    phone_no = models.CharField(max_length=12, default="None")
    blogger_group = models.CharField(max_length=50)
    profile_photo = models.ImageField(upload_to='images/profile_pic/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    following = models.ManyToManyField('self', default=None)


class Blog(models.Model):
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    upload_img = models.ImageField(upload_to='images/blog_pic/')
