from django.shortcuts import render, HttpResponse, redirect
from .models import About, Cv
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError


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
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            print("form is valid")
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "home_page/contact_form.html", {'form': form})


def success(request):
    return HttpResponse('Thank for your message!')
