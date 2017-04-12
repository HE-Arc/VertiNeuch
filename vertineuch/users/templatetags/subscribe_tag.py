from django import template

register = template.Library()


@register.simple_tag
def subscribe(user, lesson):
    if lesson in user.subscribed_lessons.all():
        user.subscribed_lessons.remove(lesson)
    else:
        user.subscribed_lessons.add(lesson)
