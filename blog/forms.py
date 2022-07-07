from ckeditor.fields import RichTextField
from django import forms
from .models import *
from blog.models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = ('title', 'article', 'categorie')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title of your Question',
                                            'class': 'p-3 mt-2 mb-4 w-full bg-slate-200 rounded border-2 border-slate-200 focus:border-slate-600 focus:outline-none'}),
            'questions': RichTextField(),
            'tags': forms.TextInput(attrs={'placeholder': 'Separate by commas',
                                           'class': 'w-full p-3 mt-2 mb-4 w-full bg-slate-200 rounded border-2 border-slate-200 focus:border-slate-600 focus:outline-none'}),

            'updates': forms.CheckboxInput(attrs={'class': 'mr-3 form-check-input h-4 w-4 border border-gray-300 rounded-sm bg-white checked:bg-blue-600 checked:border-blue-600 transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain float-left mr-2 cursor-pointer'})
        }