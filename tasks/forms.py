from django import forms
from django.forms import ModelForm
from .models import Task, Note


class CreateNewTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el titulo'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escriba una descripción'}),
            'important': forms.CheckboxInput(attrs={'class':'form-check-input m-auto'}), 
        }

class CreateNewNote(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['description',]