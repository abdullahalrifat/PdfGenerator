from django import forms
from django.forms import ModelForm

from .models import Comment


class AddCommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['message']

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'name': 'message',
                'rows': 2,
                'cols': 10,
            }
        )
    )
