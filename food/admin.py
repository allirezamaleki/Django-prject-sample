from django.contrib import admin

from food.models import Item
from .models import Item

# Register your models here.
admin.site.register(Item)