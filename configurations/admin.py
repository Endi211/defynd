from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(AreaType)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(ConstraintType)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(CultureType)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(DisputeMatter)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(DisputeObject)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(ReclamationInterventionType)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(UrbanDestination)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name']
