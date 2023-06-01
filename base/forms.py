from django import forms
from .models import Comment, Reply


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user_name',  'email', 'home_page', 'captcha', 'text']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['user_name',  'email', 'home_page', 'captcha', 'text']
