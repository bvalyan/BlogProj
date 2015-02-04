from django import forms
from django.core.exceptions import ValidationError
from testApp.models import *

class PostForm(forms.ModelForm):
  text = forms.CharField(widget=forms.Textarea, label='Entry')
  class Meta:
    model = Post;
class UserForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label='Entry')