from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Service(models.Model):
    title = models.CharField(max_length=200, unique=True)
    no_days = models.IntegerField()
    nails = models.BooleanField(default=False)
    teeth = models.BooleanField(default=False)
    bath = models.BooleanField(default=False)
    hair_cuts = models.BooleanField(default=False)
    pickup = models.BooleanField(default=False)
    price = models.IntegerField()

    def __str__(self):
        return self.title
