# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
