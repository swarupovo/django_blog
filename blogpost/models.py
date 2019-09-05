from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from blogpost.validate import max_image_cheque


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
    title = models.CharField(max_length=100, default="Django Post", blank=True)
    content = models.TextField(blank=False)
    # upload_img = models.ImageField(upload_to='images/blog_pic/')
    like = models.ManyToManyField(Blogger, related_name="blog_like")
    #


class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, default=1, validators=[max_image_cheque])
    images = models.ImageField(upload_to='images/positions/')


class Comments(models.Model):
    user = models.ForeignKey(Blogger, on_delete=models.CASCADE, default=1)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, default=1)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)




