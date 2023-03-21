from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Service
from .forms import ApplicationForm


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


class Application(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "application.html",
            {'application_form': ApplicationForm()}
            )
    
    def post(self, request, *args, **kwargs):

        application_form = ApplicationForm(data=request.POST)

        if application_form.is_valid():
            application_form.instance.author = request.user.username
            application_form.save()
        else:
            application_form = ApplicationForm()
        
        return render(
            request,
            'index.html'
        )
