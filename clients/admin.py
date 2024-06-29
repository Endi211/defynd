from django.contrib import admin
from .models import Customer


# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'code_', 'customer_type', 'vat_number', 'company_name', 'name', 'email', 'phone', 'mobile', 'origin',
        'is_active'
    )

    fieldsets = (
        (None, {
            'fields': (
                'hubspot_card', 'customer_type', 'company_name', 'role', 'name', 'last_name', 'fiscal_code',
                'vat_number')
        }),
        ('Personal Info', {
            'fields': ('birth_place', 'birthday', 'gender')
        }),
        ('Contact Info', {
            'fields': ('email', ('phone_prefix', 'phone'), ('mobile_prefix', 'mobile'))
        }),
        ('Address', {
            'fields': ('street', 'city', 'post_number', 'is_customer')
        }),
    )

    radio_fields = {
        'gender': admin.VERTICAL
    }

    list_filter = ('customer_type', 'company_name', 'gender', 'birth_place', 'is_customer', 'vat_number')

    search_fields = ['name']

    def code_(self, obj):
        return f'C0{obj.code}'

    class Media:
        css = {
            'all': ('css/admin/client_admin.css',)
        }


