# Django offers a very rich and secure API to handle forms.
# Since the form input will be saved in the database models we are gonna use the Django’s ModelForm.
# https://djangocentral.com/creating-comments-system-with-django/

from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')