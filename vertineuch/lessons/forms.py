from django import forms
from .models import Lesson


class LessonChangeForm(forms.ModelForm):

    start_date = forms.DateField(widget=forms.SelectDateWidget())
    end_date = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = Lesson
        fields = ['name', 'description', 'activity', 'difficulty', 'price', 'time', 'start_date', 'end_date', 'frequency' ]


class LessonCreationForm(forms.ModelForm):

    start_date = forms.DateField(widget=forms.SelectDateWidget())
    end_date = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = Lesson
        fields = ['name', 'description', 'activity', 'difficulty', 'price', 'time', 'start_date', 'end_date', 'frequency' ]
