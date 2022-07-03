from django import forms
from .models import *
from blog.models import *


class QuestionForm(forms.ModelForm):
    class Meta:
        model = question
        fields = ('title', 'questions', 'tags', 'updates')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title of your Question',
                                            'class': 'p-3 mt-2 mb-4 w-full bg-slate-200 rounded border-2 border-slate-200 focus:border-slate-600 focus:outline-none'}),
            'questions': RichTextField(),
            'tags': forms.TextInput(attrs={'placeholder': 'Separate by commas',
                                           'class': 'w-full p-3 mt-2 mb-4 w-full bg-slate-200 rounded border-2 border-slate-200 focus:border-slate-600 focus:outline-none'}),

            'updates': forms.CheckboxInput(attrs={'class': 'mr-3 form-check-input h-4 w-4 border border-gray-300 rounded-sm bg-white checked:bg-blue-600 checked:border-blue-600 transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain float-left mr-2 cursor-pointer'})
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = question
        fields = ('title', 'questions', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title of your Question',
                                            'class': 'p-3 mt-2 mb-4 w-full bg-slate-200 rounded border-2 border-slate-200 focus:border-slate-600 focus:outline-none'}),
            'questions': forms.Textarea(attrs={'placeholder': 'Describe about your Question',
                                               'class': 'p-3 mt-2 mb-4 w-full bg-slate-200 rounded border-2 border-slate-200 focus:border-slate-600 focus:outline-none resize-none'}),
            'tags': forms.TextInput(attrs={'placeholder': 'Separate by commas',
                                           'class': 'w-full p-3 mt-2 mb-4 w-full bg-slate-200 rounded border-2 border-slate-200 focus:border-slate-600 focus:outline-none'})
        }
