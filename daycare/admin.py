from django.contrib import admin
from .models import Service, Application

admin.site.register(Service)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('dog_name',)}
    list_display = ('dog_name', 'slug', 'status', 'created_on')
