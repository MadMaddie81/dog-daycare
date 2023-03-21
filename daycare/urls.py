from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('services/', views.Services.as_view(), name='services'),
    path('application/', views.Application.as_view(), name='application'),
]
