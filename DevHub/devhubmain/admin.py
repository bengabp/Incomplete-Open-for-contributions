from cProfile import Profile
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Post, Comment, FrequentlyAskedQuestion, Like, DevhubAccount
from .forms import DevhubAccountChangeForm, DevhubAccountCreationForm


class DevhubAdmin(UserAdmin):
    add_form = DevhubAccountCreationForm
    form = DevhubAccountChangeForm
    model = DevhubAccount
    list_display = ["username", "email", 'first_name', 'last_name', 'password', 'profile_picture_web_path',
                    'github_profile_url',
                    'linkedin_profile_url']


admin.site.register(DevhubAccount, DevhubAdmin)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(FrequentlyAskedQuestion)
admin.site.register(Like)
