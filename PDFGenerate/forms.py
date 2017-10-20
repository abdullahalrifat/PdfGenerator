from django import forms
from django.forms import ModelForm

from .models import Comment
from .models import pdf


class AddCommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['message']



class AddIdForm(ModelForm):

    class Meta:
        model = pdf
        fields = ['name','org','talk','person_image']

