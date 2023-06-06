from django import forms
from .models import Comment, Reply
from captcha.fields import CaptchaField
from ckeditor.widgets import CKEditorWidget


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = ['user_name',  'email', 'home_page', 'captcha', 'upload', 'text']

    def clean_upload(self):
        upload = self.cleaned_data.get('upload')
        if upload:
            valid_extensions = ['jpg', 'jpeg', 'png', 'txt']
            extension = upload.name.split('.')[-1].lower()
            if extension not in valid_extensions:
                raise forms.ValidationError('Тільки JPG, JPEG,  PNG та TXT дозволено.')
            if upload.size > 100 * 1024 and extension == 'txt':
                raise forms.ValidationError('Розмір файлу повинен бути не більше 100 KB.')

        return upload

class ReplyForm(forms.ModelForm):
    captcha = CaptchaField()
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Reply
        fields = ['user_name',  'email', 'home_page', 'captcha', 'upload', 'text']

    def clean_upload(self):
        upload = self.cleaned_data.get('upload')
        if upload:
            valid_extensions = ['jpg', 'jpeg', 'png', 'txt']
            extension = upload.name.split('.')[-1].lower()
            if extension not in valid_extensions:
                raise forms.ValidationError('Тільки JPG, JPEG,  PNG та TXT дозволено.')
        return upload