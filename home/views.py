from django.shortcuts import render
from django.http import HttpResponseServerError

def about(request):
    try:
        return render(request, "about.html", {"title": "About Our Restaurant"})
    except Exception as e:
        # Log the error if you have logging configured
        return HttpResponseServerError("An error occurred while loading the About page.")
