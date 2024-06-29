from django.contrib import admin
from .models import Litigation


# Register your models here.

@admin.register(Litigation)
class LitigationAdmin(admin.ModelAdmin):
    # add_form_template = 'litigation_app/admin_add_litigation.html'
    # change_form_template = 'litigation_app/admin_add_litigation.html'



    list_display = (
        'litigation_code_', 'date', 'customer', 'dispute_matter',
        'initial_estimation_value_', 'target_value_', 'registration_type', 'is_closed', 'origin'
    )

    radio_fields = {
        'reception_act': admin.VERTICAL, 'purchase_contract': admin.VERTICAL, 'fruit_pendants': admin.VERTICAL,
        'batch_disfiguration': admin.VERTICAL, 'social_economic_reform': admin.VERTICAL,
        'residual_airspace': admin.VERTICAL,
        'total_demolition': admin.VERTICAL, 'storage_state': admin.VERTICAL, 'productive_activities': admin.VERTICAL,
        'lease_agreement': admin.VERTICAL, 'need_transfer_user': admin.VERTICAL,
        'reclamation_activities': admin.VERTICAL,
    }

    list_filter = (
        'date', 'dispute_matter', 'dispute_object', 'registration_type', 'lawyer_reference', 'area_address',
        'reception_act', 'date_receipt_act', 'purchase_contract', 'contract_date', 'culture_type', 'fruit_pendants',
        'cultivator_type', 'social_economic_reform', 'urban_destination', 'epoch_construction', 'residual_airspace',
        'storage_state', 'lease_agreement', 'contract_duration', 'residual_rent', 'reclamation_intervention_type',
        'is_closed',
    )

    exclude = ['email']

    fieldsets = (
        (None, {
            'fields': (
                'is_closed', ('customer', 'value_list'), 'hyperlink_to_economics_sheet', 'upload_contract',
            )
        }),
        ('Reference', {
            'fields': ('lawyer_reference', 'reference')
        }),
        ('Other Information', {
            'fields': ('reception_act', 'date_receipt_act', 'purchase_contract', 'contract_date')
        }),
        ('Dispute', {
            'fields': ('dispute_matter', 'dispute_object', 'starting_date', 'target_date', 'closing_date')
        }),
        ('Value', {
            'fields': ('initial_estimation_value', 'target_value', 'final_value', 'revenue', 'total_cost', 'EBIT',
                       'EBIt_percentage', 'fee_percentuale')
        }),
        ('Registration', {
            'fields': ('registration_type', 'prejudicial_registrations', 'enrollment_amount')
        }),
        ('Area', {
            'fields': ('surface_directly_concerned', 'occupied_area', 'residual_surface', 'area_address',
                       'technical_reference')
        }),
        ('Information Culture', {
            'fields': ('culture_type', 'above_ground_quantification', 'fruit_pendants', 'cultivator_type',
                       'batch_disfiguration', 'description')
        }),
        ('Free Residential Industrial Expropriation', {
            'fields': (
                ('social_economic_reform', 'urban_destination'), 'transformation_coefficient', 'IMU_final_declaration',
            )
        }),
        ('Expropriation Residential Industrial Building', {
            'fields': (
                ('epoch_construction', 'building_titles'), ('extension_MQ', 'residual_airspace', 'MC_residui'),
                ('total_demolition', 'partial_demolition'), ('storage_state', 'productive_activities'),
                ('lease_agreement', 'contract_duration'), ('contract_fee', 'residual_rent'),
                ('need_transfer_user', 'reclamation_activities'), ('reclamation_intervention_type', 'reclamation_cost')
            )
        }),
    )

    class Media:
        css = {
            'all': ('css/admin/admin_styles.css',)
        }

    def target_value_(self, obj):
        # obj is the Model instance

        # If your locale is properly set, try also:
        # locale.currency(obj.amount, grouping=True)
        if obj.target_value:
            return f'{obj.target_value} €'
        return '0 €'

    def initial_estimation_value_(self, obj):

        if obj.initial_estimation_value:
            return f'{obj.initial_estimation_value} €'
        return '0 €'

    def litigation_code_(self, obj):

        return f'L0{obj.litigation_code}'

    # def change_view(self, request, object_id, form_url='', extra_context=None):
    #
    #     l_mod = Litigation.objects.latest('litigation_code')
    #
    #     extra_context = {
    #         'lmod': l_mod,
    #         'oId': object_id,
    #     }
    #     print('hellooooooooo')
    #     return super().change_view(
    #         request, object_id, form_url, extra_context=extra_context,
    #     )
