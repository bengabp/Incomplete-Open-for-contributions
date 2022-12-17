from django.template import Library
from django.templatetags.static import static
from ..models import DevhubAccount

register = Library()


@register.filter(name="get_user_profile_pic_path_from_id")
def get_profile_pic_from_id(user_id):
    return DevhubAccount.objects.get(id=user_id).profile_pic.url
