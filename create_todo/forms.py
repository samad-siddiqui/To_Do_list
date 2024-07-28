from django import forms


class CreateForm(forms.Form):
    """Form for creating a new todo"""
    
    title = forms.CharField(max_length=150) 
    description = forms.CharField(widget=forms.Textarea)
    