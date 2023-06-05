from django import forms
from .models import Comment, Reply
from captcha.fields import CaptchaField


class CommentForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = ['user_name',  'email', 'home_page', 'captcha', 'text']


class ReplyForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Reply
        fields = ['user_name',  'email', 'home_page', 'captcha', 'text']
