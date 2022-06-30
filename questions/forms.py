from django import forms
from .models import *
from blog.models import *


class QuestionForm(forms.ModelForm):
    class Meta:
        model = question
        fields = ('title', 'questions', 'categorie')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title of your Question','class': 'p-3 mt-2 mb-4 w-full bg-slate-200 rounded border-2 border-slate-200 focus:border-slate-600 focus:outline-none'}),
            'questions': forms.Textarea(attrs={'placeholder': 'Describe about your Question','class': 'p-3 mt-2 mb-4 w-full bg-slate-200 rounded border-2 border-slate-200 focus:border-slate-600 focus:outline-none resize-none'}),
            'categorie': forms.Select(attrs={'class': 'w-full p-3 mt-2 mb-4 w-full bg-slate-200 rounded border-2 border-slate-200 focus:border-slate-600 focus:outline-none'}),
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = question
        fields = ('title','questions', 'categorie')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title of your Question','class': 'p-3 mt-2 mb-4 w-full bg-slate-200 rounded border-2 border-slate-200 focus:border-slate-600 focus:outline-none'}),
            'questions': forms.Textarea(attrs={'placeholder': 'Describe about your Question','class': 'p-3 mt-2 mb-4 w-full bg-slate-200 rounded border-2 border-slate-200 focus:border-slate-600 focus:outline-none resize-none'}),
            'categorie': forms.Select(attrs={'class': 'w-full p-3 mt-2 mb-4 w-full bg-slate-200 rounded border-2 border-slate-200 focus:border-slate-600 focus:outline-none'}),
        }

