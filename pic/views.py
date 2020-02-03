# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from .models import Image, Location, Category


def home(request):
    return render(request, 'home.html')


def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "image": searched_image})
    else:
        message: "Search your location photos"
        return render(request, 'search.html', {"message": message})
# Create your views here.
