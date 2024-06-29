from django.contrib import admin
from .models import Lawyer

# Register your models here.


@admin.register(Lawyer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name']
