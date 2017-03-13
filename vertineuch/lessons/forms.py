from django import forms
from .models import Lesson


class LessonChangeForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['name', ]

class LessonCreationForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['name', ]
