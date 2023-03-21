from .models import Application
from django import forms


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'package',
            'dog_name',
            'breed',
            'weight',
            'height',
            'gender',
            'neutered',
            'insured',
            'vaccinated',
            'experience',
            'info',
            'owner_first_name',
            'owner_last_name',
            'email',
        ]
        labels = {
            'package': "Pick a Daycare Package:",
            'dog_name': "Dog's name:",
            'breed': "Breed:",
            'weight': "Weight:",
            'height': "Height:",
            'gender': "Gender",
            'neutered': "My dog is neutered / spayed",
            'insured': "My dog is insured",
            'vaccinated': "My dog is fully vaccinated",
            'experience': "My dog has previous experience from daycare",
            'info': "Please tell us a bit about your dog:",
            'owner_first_name': "Owner's first name:",
            'owner_last_name': "Owner's last name:",
            'email': "Email:",
        }