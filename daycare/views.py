from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Service


class Home(generic.View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "index.html"
            )


# class Services(generic.ListView):
#     model = Service
#     queryset = Service.objects.all()
#     template_name = 'services.html'

def services(request):
    deals = Service.objects.all()
    context = {
        'deals': deals
    }
    return render(request, 'services.html', context)