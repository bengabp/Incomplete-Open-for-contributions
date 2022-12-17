from django.contrib import admin
from .models import FavouriteMentalItem,Task

# Register your models here.
admin.site.register(Task) # Register Task Model
admin.site.register(FavouriteMentalItem) # Register FavouriteMentalItem Model

