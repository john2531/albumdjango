# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
    """ Categorias para clasificar las fotos """
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name 

class Photo(models.Model):
    """ Fotos del album """
    category = models.ForeignKey(Category, null=True, blank=True)
    title = models.CharField(max_length=50, default='No title')
    photo = models.ImageField(upload_to='photos/')
    pub_date = models.DateField(auto_now_add=True)
    favorite = models.BooleanField(default=False)
    comment = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.title
