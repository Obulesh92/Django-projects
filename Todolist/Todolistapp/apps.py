# Todolistapp/apps.py
from django.apps import AppConfig

class TodolistappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Todolistapp'      # ← this must match