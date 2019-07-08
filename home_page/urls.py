from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about/', views.about_view, name='about-view'),
    path('cv/', views.cv_view, name='cv-view'),
    path('contact/', views.email, name='contact'),
    path('projects/', views.projects, name='projects'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)