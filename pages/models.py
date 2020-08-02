from django.db import models
from django.urls import reverse

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=120)
    picture = models.ImageField(upload_to='profile/')
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("about", kwargs={id: self.id})


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()