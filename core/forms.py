from django import forms
from .models import *

class edit_profile_form(forms.ModelForm):
    class Meta:
        model = employe_details
        fields = ['about', 'skills', 'experience', 'education']