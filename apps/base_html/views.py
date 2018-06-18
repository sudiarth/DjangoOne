from django.shortcuts import render

def index(request):
    return render(request, 'base_html/index.html')