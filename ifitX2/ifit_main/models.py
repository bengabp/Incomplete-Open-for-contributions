from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    title = models.TextField(max_length=100,default=None)
    description =  models.TextField(max_length=200,default=None)
    created_at = models.DateTimeField(auto_now=True)



class FavouriteMentalItem(models.Model):
    category = models.TextField(max_length=10)

    joke = models.TextField()

    quote = models.TextField()
    author = models.TextField()

    riddle = models.TextField()
    answer = models.TextField()

    fact = models.TextField()
    
    created_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    unique_hash = models.TextField(unique=True)


