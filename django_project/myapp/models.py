# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid


# Create your models here.
class usermode(models.Model):

    name= models.CharField(max_length=255)
    username= models.CharField(max_length=30)
    phone= models.CharField(max_length=20)
    created_on= models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    email= models.EmailField(max_length=20)
    password=models.CharField(max_length=30)


class sessiontoken(models.Model):
    user=models.ForeignKey(usermode)
    session_token=models.CharField(max_length=255)
    created_on=models.DateTimeField(auto_now_add=True)
    is_valid=models.BooleanField(default=True)
    def create_token(self):
        self.session_token=uuid.uuid4()


