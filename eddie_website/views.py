from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, "homepage.html")


def contactpage(request):
    return render(request, "contactpage.html")


def musicpage(request):
    return render(request, "musicpage.html")


def gamespage(request):
    return render(request, "gamespage.html")
