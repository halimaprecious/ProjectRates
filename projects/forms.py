from django import forms
from .models import *
from django.contrib.auth.models import User



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
          'bio': forms.Textarea(attrs={'rows':2, 'cols':10,}),
        }


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['owner', 'post_date', 'profile']
        widgets = {
          'description': forms.Textarea(attrs={'rows':4, 'cols':10,}),
        }
        
