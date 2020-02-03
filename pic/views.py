# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Image, Location, Category


def home(request):
    image = Image.image()
    return render(request, 'base.html', {"image": image})


def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "images": searched_image})
    else:
        message="Search your location photos"
        return render(request, 'search.html', {"message": message})

# def image(request, image_id):
#     try:
#         image = Image.objects.get(id=image_id)
#     except DoesNotExist:
#         raise Http404()
#     return render(request, "home.html", {"image": image})
