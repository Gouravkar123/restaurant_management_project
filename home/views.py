from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseServerError


def about(request):
    context = {
        "title": settings.RESTAURANT_NAME,
        "restaurant_name": settings.RESTAURANT_NAME,
    }
    return render(request, "about.html", context)

def custom_404(request, exception=None):
    return render(request, "404.html", status=404)


