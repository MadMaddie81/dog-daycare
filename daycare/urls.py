from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('services/', views.Services.as_view(), name='services'),
    path('application/', views.ApplicationView.as_view(), name='application'),
    path('my_applications/', views.MyApplications.as_view(), name='my_applications'),
    path('edit_application/<int:pk>/', views.EditApplication.as_view(), name='edit_application')
]
