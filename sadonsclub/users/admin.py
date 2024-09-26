from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUsers


admin.site.register(CustomUsers)