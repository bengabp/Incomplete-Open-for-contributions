from django.urls import path
from . import views
from . import auth

urlpatterns = [
    path("", views.home, name="home"),
    path("posts", views.display_posts, name="posts"),
    path("login", auth.handle_login, name="login"),
    path("register", auth.handle_user_registration, name="register"),
    path("logout", auth.handle_logout, name="logout"),
    path("new-post",views.handle_newpost_creation,name="new_post")
]
