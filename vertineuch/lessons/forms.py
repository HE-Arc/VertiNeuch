from django import forms
from .models import lesson


class courForm(forms.ModelForm):
    class Meta:
        model = lesson
        fields = ['name', ]
