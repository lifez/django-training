from django.db import models


class Post(models.Model):
    text = models.CharField(max_length=256, null=False, blank=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)