from django.db import models
from .validators import validate_file_extension


# Create your models here.
class About(models.Model):
    about_me = models.TextField(default="to be updated")

    class Meta:
        verbose_name = "About Info"
        verbose_name_plural = "About Info"

    def __str__(self):
        return "About"


class Cv(models.Model):
    # TODO: create path for cv file
    cv = models.FileField(upload_to="#", validators=[validate_file_extension])

    class Meta:
        verbose_name = "CV"
        verbose_name_plural = "CV"

    def __str__(self):
        return "CV"


class Contact(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    message = models.TextField()
    date_send = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Messages"
        verbose_name_plural = "Messages"
