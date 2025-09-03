from django.shortcuts import render
from django.http import HttpResponseServerError

def about(request):
    return render(request, "about.html")

def custom_404(request, exception=None):
    return render(request, "404.html", status=404)