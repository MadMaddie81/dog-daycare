from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Service


class Home(generic.View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "index.html"
            )


class Services(generic.ListView):
    model = Service
    template_name = 'services.html'
    ordering = ['price']
