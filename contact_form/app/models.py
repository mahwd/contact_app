# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Form(models.Model):
    name = models.CharField(max_length=20, verbose_name="name")
    email = models.EmailField(max_length=30, verbose_name="Email")
    subject = models.CharField(max_length=20,verbose_name="aim")
    message = models.TextField(verbose_name='Confess')