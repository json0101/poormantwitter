# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Tweet(models.Model):
    TweetId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=25)
    Content = models.CharField(max_length=50)
    DateInsert = models.DateTimeField(default=timezone.now)