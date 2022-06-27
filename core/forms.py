from django import forms
from .models import *


class NewsletterForm(forms.ModelForm):

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "placeholder":"John Doe",
                "class": "flex-grow w-full h-12 px-4 mb-2 transition duration-200 bg-white border border-gray-300 rounded shadow-sm appearance-none focus:border-deep-purple-accent-400 focus:outline-none focus:shadow-outline"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "type": "email",
                "autocomplete": "email",
                "placeholder": "demo@example.com",
                "class": "flex-grow w-full h-12 px-4 mb-2 transition duration-200 bg-white border border-gray-300 rounded shadow-sm appearance-none focus:border-deep-purple-accent-400 focus:outline-none focus:shadow-outline"
            }
        )
    )

    class Meta:
        model = newsletter
        fields = ['name', 'email']
