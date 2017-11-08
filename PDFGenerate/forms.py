from django import forms
from django.forms import ModelForm

from .models import Comment
from .models import pdf
from .models import verify
from .models import excel


class AddCommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['message']



class AddIdForm(ModelForm):

    class Meta:
        model = pdf
        fields = ['name','org','talk','person_image']



class AddPasswordForm(ModelForm):

    class Meta:
        model = verify
        fields = ['password']


class AddExcelForm(ModelForm):

    class Meta:
        model = excel
        fields = ['ex','type']
