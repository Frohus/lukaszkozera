from django.shortcuts import render
from .models import About, Cv


# Create your views here.


def home(request):
    return render(request, 'home_page/home.html')


def about_view(request):
    about_text = About.objects.first()
    return render(request, '#', {'about_text': about_text})
