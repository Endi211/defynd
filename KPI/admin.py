from django.contrib import admin
from .models import Kpi
# from dashboard_page.models import type_1_stat, type_4_stat, type_3_stat, type_2_stat


# Register your models here.


@admin.register(Kpi)
class KpiAdmin(admin.ModelAdmin):
    change_list_template = 'kpi/kpi_admin.html'

    class Media:
        css = {
            'all': ('KPI/styles.css',)
        }

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    # def changelist_view(self, request, extra_context=None):
    #     extra_context = {
    #         'type_1_stat': type_1_stat,
    #         'type_2_stat': type_2_stat,
    #         'type_3_stat': type_3_stat,
    #         'type_4_stat': type_4_stat,
    #     }
    #
    #     return super().changelist_view(request, extra_context=extra_context)






