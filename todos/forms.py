'''importing django forms'''
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    '''todo form'''
    class Meta:
        '''class'''
        model = Todo
        fields = ['title', 'description', 'is_done']