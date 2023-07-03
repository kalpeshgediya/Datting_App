from __future__ import unicode_literals
from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
User = get_user_model()

admin.site.register(User)
admin.site.register(Upload_image)