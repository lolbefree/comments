from django.db import models
from captcha.fields import CaptchaField


class Comment(models.Model):
    user_name = models.CharField(blank=False, max_length=100, verbose_name="Користувач")
    email = models.EmailField(blank=False)
    home_page = models.URLField(blank=True, verbose_name="Домашня сторінка")
    captcha = CaptchaField(label='Введіть CAPTCHA')
    text = models.TextField(blank=False, verbose_name="коментар")
    created_at = models.DateTimeField(auto_now_add=True)


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    home_page = models.URLField(blank=True)
    captcha = CaptchaField(label='Введіть CAPTCHA')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
