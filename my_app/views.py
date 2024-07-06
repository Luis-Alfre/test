from django.shortcuts import render

def index(request):
    return render(request, 'my_app/index.html')

def create(request):
    return render(request, 'my_app/create.html')
