
from django import template
from courses.models import UserCourse


register = template.Library()

@register.simple_tag
def is_enrolled(course,user):
    if not  user.is_authenticated:
        return False
    try:
        user_course = UserCourse.objects.get(user = user, course = course)
        return True
    except:
        return False