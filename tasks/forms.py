from django import forms
from django.forms import ModelForm
from .models import Task


class CreateNewTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba el titulo'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escriba una descripción'}),
            'important': forms.CheckboxInput(attrs={'class':'form-check-input m-auto'}), 
        }

class CreateNewProject(forms.Form):
    name = forms.CharField(label='Nombre de Proyecto', max_length=200)
