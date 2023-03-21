from django.contrib import admin
from .models import Service, Application

admin.site.register(Service)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):

    list_display = ('dog_name', 'author', 'status', 'created_on')
