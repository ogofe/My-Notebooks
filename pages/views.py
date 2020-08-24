from django.shortcuts import render
from django.views.generic import (
    ListView,
    DeleteView,
    UpdateView,
)
from contestant.models import Account

# Create your views here.
def index(request):
    context = {
        'title': 'Home',
                    
    }
    return render(request, 'index.html', context)

def All(request):
    context = {
        'accounts' : Account.objects.all(),
    }
    return render(request, 'all.html', context)

def Del(request):
    context = {
        'accounts' : Account.objects.all(),
    }
    return render(request, 'all.html', context)

def Up(request):
    context = {
        'accounts' : Account.objects.all(),
    }
    return render(request, 'all.html', context)