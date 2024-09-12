from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request: HttpResponse):
    context = {}
    return render(request, 'index.html', context)

def index(request: HttpResponse, unit:str=None):
    if unit == None:
        return redirect('home')
    context = {}
    return render(request, 'converter.html', context)