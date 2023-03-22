from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Service, Application
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


class ApplicationView(View):

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


class MyApplications(generic.ListView):

    def get(self, request, *args, **kwargs):
        apps = Application.objects.filter(author=request.user.username)
        return render(
            request,
            'view_application.html',
            {'apps': (apps)}
        )
