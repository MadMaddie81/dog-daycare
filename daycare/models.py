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


class Application(models.Model):

    STATUS = [
        (0, 'Pending'),
        (1, 'Approved'),
        (3, 'Rejected')
    ]

    WEIGHT_CHOICES = [
        (None, 'Pick a choice'),
        ('Mini', 'Mini (< 2 kg)'),
        ('Small', 'Small (2-8 kg)'),
        ('Medium', 'Medium (8-15 kg)'),
        ('Large', 'Large (> 15 kg)')
    ]

    HEIGHT_CHOICES = [
        (None, 'Pick a choice'),
        ('Mini', 'Mini (< 25 cm)'),
        ('Small', 'Small (25-36 cm)'),
        ('Medium', 'Medium (36-45 cm)'),
        ('Large', 'Large (> 45 cm)')
    ]

    GENDER_CHOICES = [
        (None, 'Pick a choice'),
        ('Male', 'Male'),
        ('Female', 'Female')
    ]

    dog_name = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, default='', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    breed = models.CharField(max_length=200, blank=False, default='')
    weight = models.CharField(
        max_length=10,
        choices=WEIGHT_CHOICES,
        default=None
        )
    height = models.CharField(
        max_length=10,
        choices=HEIGHT_CHOICES,
        default=None
        )
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default=None
        )
    neutered = models.BooleanField(default=False)
    insured = models.BooleanField(default=False)
    vaccinated = models.BooleanField(default=False)
    experience = models.BooleanField(default=False)
    info = models.TextField()
    owner_first_name = models.CharField(max_length=200, blank=False)
    owner_last_name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(blank=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.slug
