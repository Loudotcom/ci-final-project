from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Field
from django.forms import ModelForm
from .models import Task

class TaskForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add in a new task'}))

    class Meta:
        model = Task
        fields = ['name']
    
