from django.contrib import admin
from .models import Menu
from .models import MenuCategory


# Register your models here.
# This is admin.py file which is a part of myapp app
# it is used to register the models of the app

admin.site.register(MenuCategory)
admin.site.register(Menu)