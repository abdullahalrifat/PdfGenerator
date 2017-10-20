from django import forms
from django.forms import ModelForm

from .models import Comment
from .models import pdf


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

class AddIdForm(ModelForm):

    class Meta:
        model = pdf
        fields = ['name','org','talk','person_image']

    name = forms.CharField(widget=forms.Textarea(
            attrs={
                'name': 'name',
                'rows': 2,
                'cols': 10,
            }
        )
    )
    org = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'name': 'org',
                'rows': 2,
                'cols': 10,
            }
        )
    )
    talk = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'name': 'talk',
                'rows': 2,
                'cols': 10,
            }
        )
    )
    person_image =forms.ImageField(label = 'Choose your image',
                                          help_text = 'The image should be cool.')
