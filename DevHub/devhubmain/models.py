from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class DevhubAccount(AbstractUser):
    username = models.CharField(max_length=20,unique=True)
    profile_picture_web_path = models.CharField(max_length=1000)
    profile_pic = models.ImageField(upload_to = "profiles")

    github_profile_url = models.CharField(max_length=1000)
    linkedin_profile_url = models.CharField(max_length=1000)

    def _str__(self):
        return f"<DevhubAccount @{self.username}"


class Post(models.Model):
    creator_id = models.IntegerField()
    title = models.CharField(max_length=500)
    body = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now=True)
    post_image_url = models.CharField(max_length=1000)

    def __str__(self):
        return f"<Post Object> {self.title}"


class Comment(models.Model):
    creator_id = models.IntegerField()
    body = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Comment Object> {self.body}"


class FrequentlyAskedQuestion(models.Model):
    title = models.CharField(max_length=500)
    body = models.CharField(max_length=1000)

    def __str__(self):
        return f"<FAQ Object> {self.title}"


class Like(models.Model):
    creator_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
