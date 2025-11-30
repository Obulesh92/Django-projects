# project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_todos(request):
    return redirect('todo_list')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include('Todolistapp.urls')),
    path('', redirect_to_todos),   # ← This fixes the 404 on root URL
]