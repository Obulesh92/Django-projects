# your_app_name/forms.py
from django import forms
from .models import MyVideo

class VideoForm(forms.ModelForm):
    class Meta:
        model = MyVideo
        fields = ['title', 'video']
