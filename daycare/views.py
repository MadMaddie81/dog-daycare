from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
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


class EditApplication(UpdateView):

    model = Application
    template_name = 'edit_application.html'
    fields = (
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
        )
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('my_applications')


class DeleteApplication(DeleteView):
    model = Application
    template_name = 'delete_application.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('my_applications')
