from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'lecture1/index.html')
    
def hello(request):
    return render(request,'lecture1/hello.html')

def headings(request):
    return render (request,'lecture1/headings.html')

def lists(request):
    return render (request,'lecture1/lists.html')

def image(request):
    return render (request,'lecture1/image.html')

def link(request):
    return render (request,'lecture1/link.html')

def table(request):
    return render (request,'lecture1/table.html')

def form(request):
    return render (request,'lecture1/form.html')

def style(request):
    return render (request,'lecture1/style.html')


def alper(request):
    return HttpResponse("Hello Alper!")
