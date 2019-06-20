from django.shortcuts import render, HttpResponse
from .models import About, Cv
from django.http import FileResponse, Http404


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
        'cv_views': Cv.objects.all()
    }
    return render(request, 'home_page/cv.html', context)

# def cv_view(request):
#     with open("home_page/static/home_page/examplepdf.pdf", "r") as pdf:
#         response = HttpResponse(pdf.read(), mimetype="application/pdf")
#         response["Content-Disposition"] = "inline;filename=home_page/static/home_page/examplepdf.pdf"
#         return response
