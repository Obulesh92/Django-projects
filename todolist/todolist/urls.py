"""
URL configuration for todolist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static 
from django.conf import  settings 
from Todolistapp.views import Todolist,add_task,edit_task,delete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Todolist,name="Todolist"),
    path('addtask/',add_task,name="addtask"),
    path('edit_task/<str:id>',edit_task,name='edittask'),
    path('delete_task/<str:id>',delete_task,name='deletetask')
]

if settings.DEBUG: 
    urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 

