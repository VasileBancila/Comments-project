from django import forms
from .models import Comments

class CommentsForm(forms.ModelForm): # method save() specific ModelForm
    class Meta:
        model = Comments
        fields = ['comment']