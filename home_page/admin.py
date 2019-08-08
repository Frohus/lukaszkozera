from django.contrib import admin
from .models import About, Cv, Project, Technology

# Register your models here.
admin.site.register(About)
admin.site.register(Cv)
admin.site.register(Project)
admin.site.register(Technology)