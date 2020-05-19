from django.shortcuts import render

# Create your views here.

def index(request):
    """Returns the Index.html file"""
    return render(request, 'index.html')