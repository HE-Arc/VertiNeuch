from django.contrib import admin
from django.contrib.admin import ModelAdmin

from vertineuch.lessons.forms import LessonChangeForm, LessonCreationForm
from .models import Lesson


class MyLessonChangeForm(LessonChangeForm):
    class Meta(LessonChangeForm.Meta):
        model = Lesson


class MyLessonCreationForm(LessonCreationForm):
    class Meta(LessonCreationForm.Meta):
        model = Lesson


@admin.register(Lesson)
class MyLessonAdmin(ModelAdmin):
    form = MyLessonChangeForm
    add_form = MyLessonCreationForm
    fieldsets = (

    )
    list_display = ()
    search_field = []
