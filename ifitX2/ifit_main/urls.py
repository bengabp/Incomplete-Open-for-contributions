from django.contrib import admin
from django.urls import path,include
from .auth import handle_login,handle_register,handle_logout
from .views import (dashboard,fitness,
                    favourites,receipes,
                    mental,get_facts,get_riddles,
                    get_jokes,get_quotes)

urlpatterns = [
    path('login',handle_login,name="login"),
    path('register',handle_register,name="register"),
    path("logout",handle_logout,name="logout"),
    path('',dashboard,name="dashboard"),
    path("dashboard",dashboard,name="dashboard"),
    path("fitness",fitness,name="fitness"),
    path("favourites",favourites,name="favourites"),
    path("receipes",receipes,name="receipes"),
    path("mental",mental,name="mental"),

    path("get-facts",get_facts,name="get_facts"),
    path("get-riddles",get_riddles,name="get_riddles"),
    path("get-jokes",get_jokes,name="get_jokes"),
    path("get-quotes",get_quotes,name="get_quotes"),
]
