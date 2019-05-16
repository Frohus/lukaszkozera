from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about/', views.about_view, name='about-view'),
    path('cv/', views.cv_view, name='cv-view')
]