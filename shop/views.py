from django.shortcuts import render

# Create your views here.

def shop(request):
    """A view that displays the index page"""
    return render(request, "shop.html")
    