from django.contrib import admin
from django.contrib.admin.utils import flatten_fieldsets

from .models import Statistic


# Register your models here.


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'number', 'initial_value', 'objective_value',
        'final_value', 'moltiplicatore', 'revue_value', 'total_cost_value', 'EBIT', 'EBIt_percent',
    )

    list_display_links = None

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
