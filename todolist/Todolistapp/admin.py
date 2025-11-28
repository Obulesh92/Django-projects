from django.contrib import admin
from .models import Todo_data
# Register your models here.
# Removed the trailing dot that caused "Expected attribute name after '.'" syntax error.
admin.site.register(Todo_data)
# admin.register