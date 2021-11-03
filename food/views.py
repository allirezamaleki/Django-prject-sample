from django import template
from django.db import models
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import ItemForm
from .models import Item
from django.template import context, loader


# Create your views here.

def index(request):
    item_list = Item.objects.all()
    # template = loader.get_template("food/index.html")
    context = {
        'item_list': item_list,
    }
    return render(request, 'food/index.html', context)
    # return HttpResponse(template.render(context, request))

def item(request):
    return HttpResponse("These are the items.")

def detail(request, item_id):
    item = Item.objects.get(pk = item_id)
    context = {
        'item': item,
    }
    # return HttpResponse("This is item no/id: %s" % item_id)
    return render(request, 'food/detail.html', context)


def create_item(request):
    form = ItemForm(request.POST or None)
    context = {
        'form': form,
    }
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', context)