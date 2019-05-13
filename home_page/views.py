from django.shortcuts import render
from .models import About, Cv


# Create your views here.


def home(request):
    context = {
        'about': About.objects.all()
    }
    return render(request, 'home_page/home.html', context)