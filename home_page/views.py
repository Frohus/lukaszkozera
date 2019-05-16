from django.shortcuts import render
from .models import About, Cv


# Create your views here.


def home(request):
    return render(request, 'home_page/home.html')


def about_view(request):
    context = {
        'about_texts': About.objects.all()
    }
    return render(request, 'home_page/modal.html', context)


def cv_view(request):
    context = {
        'cv_display': Cv.objects.all()
    }
    return render(request, 'home_page/cv.html', context)