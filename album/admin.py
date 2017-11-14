# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from album.models import Category, Photo

import sys 
reload(sys)
sys.setdefaultencoding('utf-8')

# Register your models here.
admin.site.register(Category)
admin.site.register(Photo)


