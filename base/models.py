from django.core.validators import FileExtensionValidator
from django.db import models
from captcha.fields import CaptchaField
import os
from django.db import models
from PIL import Image


def upload_to(instance, filename):
    # Generate a new filename with the row's primary key (pk)
    if instance.pk:
        filename = f'{instance.pk}_{filename}'
    return os.path.join('%Y/%m/%d/', filename)


class Comment(models.Model):
    user_name = models.CharField(blank=False, max_length=100, verbose_name="Користувач")
    email = models.EmailField(blank=False)
    home_page = models.URLField(blank=True, verbose_name="Домашня сторінка")
    captcha = CaptchaField(label='Введіть CAPTCHA')
    text = models.TextField(blank=False, verbose_name="коментар")
    created_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to="%Y/%m/%d/", blank=True,
                              validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'txt'])])

    def __str__(self):
        return self.user_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.upload and self.upload.name.lower().endswith(('.jpg', '.jpeg', '.png')) and os.path.isfile(
                self.upload.path):
            image = Image.open(self.upload.path)
            max_width = 320
            max_height = 240
            image.thumbnail((max_width, max_height))
            image.save(self.upload.path)


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    home_page = models.URLField(blank=True)
    captcha = CaptchaField(label='Введіть CAPTCHA')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to="%Y/%m/%d/", blank=True,
                              validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'txt'])])

    def __str__(self):
        return self.user_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.upload and self.upload.name.lower().endswith(('.jpg', '.jpeg', '.png')) and os.path.isfile(
                self.upload.path):
            image = Image.open(self.upload.path)
            max_width = 320
            max_height = 240
            image.thumbnail((max_width, max_height))
            image.save(self.upload.path)
