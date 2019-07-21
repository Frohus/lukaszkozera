from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.core.exceptions import ValidationError

from .models import About, Cv
from .forms import ContactForm
from lukaszkozera.secrets import INBOX_EMAIL

# Create your views here.


def home(request):
    return render(request, 'home_page/home.html')


def about_view(request):
    context = {
        'about_texts': About.objects.all()
    }
    return render(request, 'home_page/about.html', context)


def cv_view(request):
    context = {
        'cv_views': Cv.objects.all()
    }
    return render(request, 'home_page/cv.html', context)


def email(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = form.cleaned_data["from_email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"] + \
                      f"\nSend from: {mail}"
            send_mail(subject, message, mail, [INBOX_EMAIL], fail_silently=False)
            messages.success(request, "Thanks for your message")
            return redirect("homepage")
        else:
            messages.error(request, "Some error occurred while send the message.")
    #         TODO: Display success and error message
    else:
        form = ContactForm()
    return render(request, "home_page/contact_form.html", {"form": form})


def projects(request):
    return render(request, 'home_page/projects.html')
