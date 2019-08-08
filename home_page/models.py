from django.db import models
from .validators import validate_file_extension


# Create your models here.
class About(models.Model):
    about_me = models.TextField(default="to be updated")

    class Meta:
        verbose_name_plural = "About Info"

    def __str__(self):
        return "About"


class Cv(models.Model):
    cv = models.FileField(upload_to="media", validators=[validate_file_extension])

    class Meta:
        verbose_name_plural = "CV"

    def __str__(self):
        return "CV"


class Project(models.Model):
    project_title = models.CharField(max_length=50)
    project_desc = models.TextField()
    project_date_added = models.DateTimeField(auto_now_add=True)
    project_url = models.TextField(max_length=200)

    def __str__(self):
        return self.project_title


class Technology(models.Model):
    technology_name = models.CharField(max_length=30)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    technology_used = models.BooleanField(default=False)
    technology_icon = models.TextField(max_length=100)

    class Meta:
        verbose_name_plural = "Technologies"
