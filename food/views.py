from django import template
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import context, loader

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    template = loader.get_template("food/index.html")
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def item(request):
    return HttpResponse("These are the items.")

