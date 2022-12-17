from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Post, FrequentlyAskedQuestion


# Create your views here.

def home(request):
    context_dictionary = {
        'faqs': FrequentlyAskedQuestion.objects.all(),
    }
    return render(request, "devhubmain/home.html", context_dictionary)


def display_posts(request):
    context_dictionary = {
        'posts': Post.objects.all()
    }
    return render(request, "devhubmain/posts.html", context_dictionary)


def handle_newpost_creation(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            title = request.POST.get("post-title",None)
            body = request.POST.get("post-body",None)
            new_post = Post(creator_id=request.user.id,title=title,body=body,post_image_url="")
            new_post.save()
    return redirect("posts")
