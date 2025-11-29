from django.contrib import admin
from .models import MyPhoto,MyVideo,Contact
# Register your models here.
admin.site.register(MyPhoto)
admin.site.register(MyVideo)
admin.site.register(Contact)