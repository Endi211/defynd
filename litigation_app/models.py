from django.db import models
from django.utils import timezone

from clients.models import Customer
from lawyers_app.models import Lawyer
from configurations.models import DisputeMatter, DisputeObject, CultureType, UrbanDestination, \
    ReclamationInterventionType

from django.utils.translation import gettext_lazy as _

# Create your models here.


value_choices = (
    ('25%', '25%'),
    ('50%', '50%'),
    ('75%', '75%'),
    ('90%', '90%'),
    ('100%', '100%'),
)

yes_no_choice = (
    ('Yes', _('Yes')),
    ('No', 'No')
)


registration_types = (
    ('Esproprio Agricolo', 'Agricultural Export'),
    ('Esproprio Residenziale Libera', 'Expropriation Residential Industrial Building'),
    ('Esproprio Industriale Libera','Expropriation Residential Industrial Building'),
    ('Esproprio Fabbricato Residenziale','Esproprio Fabbricato Residenziale'),
    ('Esproprio Fabbricato Industriale','Esproprio Fabbricato Industriale'),
    ('Area boschiva','Area boschiva'),
    ('Area industriale con fabbricati', 'Area industriale con fabbricati'),
    ('Area industriale senza fabbricati', 'Area industriale senza fabbricati'),
    ('Area Residenziale con fabbricati', 'Area Residenziale con fabbricati'),
    ('Area Residenziale senza fabbricati', 'Area Residenziale senza fabbricati'),
    ('Area Agricola con fabbricati', 'Area Agricola con fabbricati'),
    ('Area Agricola senza fabbricati', 'Area Agricola senza fabbricati'),
)


cultivator_choices = (
    ('Value 1', _('Value 1')),
    ('Value 2', _('Value 2')),
)


storage_state_choices = (
    ('Great', _('Great')),
    ('Good', _('Good')),
    ('Enough', _('Enough')),
    ('To be Restructured', _('To be Restructured')),
)


class Litigation(models.Model):
    litigation_code = models.AutoField(_("Litigation Code"),primary_key=True)
    is_closed = models.BooleanField(_("Closed"), default=None)
    customer = models.ForeignKey(Customer,verbose_name=_("Customer"), on_delete=models.CASCADE, null=True, blank=True)
    value_list = models.CharField(_("Value List"),max_length=10, choices=value_choices ,null=True, blank=True)
    hyperlink_to_economics_sheet = models.CharField(_("Hyperlink to economics sheet"),max_length=50 , null=True, blank=True)
    upload_contract = models.FileField(_("Upload Contract"),null=True, blank=True)
    date = models.DateTimeField(_("Date"),default=timezone.now, blank=True)
    lawyer_reference = models.ForeignKey(Lawyer, verbose_name=_("Lawyer Reference"), on_delete=models.PROTECT ,null=True, blank=True)
    reference = models.CharField(_("Reference"),max_length=50, null=True, blank=True)
    reception_act = models.CharField(_("Reception Act"),max_length=50, choices=yes_no_choice, null=True,  blank=True, default=None)
    date_receipt_act = models.DateField(_("Date Receipt Act"),max_length=50, null=True, blank=True)
    purchase_contract = models.CharField(_("Purchase Contract"),max_length=50, choices=yes_no_choice, null=True,  blank=True , default=None)
    contract_date = models.DateField(_("Contract Date"),max_length=50, null=True, blank=True)
    dispute_matter = models.ForeignKey(DisputeMatter,verbose_name=_("Dispute Matter"), on_delete=models.PROTECT, null=True, blank=True)
    dispute_object = models.ForeignKey(DisputeObject,verbose_name=_("Dispute Object"), on_delete=models.PROTECT, null=True, blank=True)
    starting_date = models.DateField(_("Starting Date"),null=True, blank=True)
    target_date = models.DateField(_("Target Date"),null=True, blank=True)
    closing_date = models.DateField(_("Closing Date"),max_length=20, null=True, blank=True)
    initial_estimation_value = models.CharField(_("Initial Estimation Value"), max_length=50, null=True, blank=True)
    target_value = models.CharField(_("Target Value"),max_length=50, null=True, blank=True)
    final_value = models.CharField(_("Final Value"),max_length=50 , null=True, blank=True)
    revenue = models.CharField(_("Revenue"),max_length=50, null=True, blank=True)
    total_cost = models.CharField(_("Total Cost"),max_length=50, null=True, blank=True)
    EBIT = models.CharField(max_length=50 , null=True, blank=True)
    EBIt_percentage = models.CharField(_("EBIT Percentage"),max_length=50,  null=True, blank=True)
    fee_percentuale = models.CharField(_("Fee Percentage"),max_length=50, null=True, blank=True)

    registration_type = models.CharField(_("Registration Type"),max_length=50, choices=registration_types, default='Agricultural Export')
    prejudicial_registrations = models.CharField(_("Prejudicial Registrations"),max_length=50 , null=True, blank=True)
    enrollment_amount = models.CharField(_("Enrollment Amount"),max_length=50 , null=True, blank=True)

    surface_directly_concerned = models.CharField(_("Surface Directly Concerned"),max_length=50 , null=True, blank=True)
    occupied_area = models.CharField(_("Occupied Area"),max_length=50 , null=True, blank=True)
    residual_surface = models.CharField(_("Residual Surface"), null=True, blank=True, max_length=50)

    area_address = models.CharField(_("Area Address"),max_length=50 , null=True, blank=True)
    technical_reference = models.CharField(_("Technical Reference"),max_length=50, null=True, blank=True)
    culture_type = models.ForeignKey(CultureType,verbose_name=_("Culture Type"), on_delete=models.PROTECT , null=True, blank=True)
    above_ground_quantification = models.CharField(_("Above Ground Quantification"),max_length=50 ,null=True, blank=True)
    fruit_pendants = models.CharField(_("Fruit Pendants"),max_length=50, choices=yes_no_choice ,  null=True, blank=True, default=None)
    cultivator_type = models.CharField(_("Cultivator Type"),max_length=50, default='Value 1', choices=cultivator_choices)

    batch_disfiguration = models.CharField(_("Batch Disfiguration"),max_length=50, choices=yes_no_choice , null=True,  blank=True, default=None)
    description = models.TextField(_("Description"), null=True, blank=True)

    social_economic_reform = models.CharField(_("Social Economic Reform"),max_length=50, choices=yes_no_choice , null=True,  blank=True, default=None)
    urban_destination = models.ForeignKey(UrbanDestination,verbose_name=_("Urban Destination"), on_delete=models.PROTECT, null=True, blank=True)
    transformation_coefficient = models.CharField(_("Transformation Coefficient"),max_length=100, null=True, blank=True)
    IMU_final_declaration = models.CharField(_("IMU Final Declaration"),max_length=100 , null=True, blank=True)

    epoch_construction = models.CharField(_("Epoch Construction"),max_length=50, null=True, blank=True)
    building_titles = models.TextField(_("Building Titles"),null=True, blank=True)
    extension_MQ = models.CharField(_("Extension MQ"),max_length=100, null=True, blank=True)

    residual_airspace = models.CharField(_("Residual Airspace"),max_length=50, choices=yes_no_choice, null=True,  blank=True, default=None)
    MC_residui = models.CharField(_("MC Residui"),max_length=50, null=True, blank=True)

    total_demolition = models.CharField(_("Total Demolition"),max_length=50, choices=yes_no_choice, null=True,  blank=True, default=None)
    partial_demolition = models.CharField(_("Partial Demolition"),max_length=100, null=True, blank=True)
    storage_state = models.CharField(_("Storage State"),max_length=100, choices=storage_state_choices, null=True, blank=True, default=None)
    productive_activities = models.CharField(_("Productive Activities"),max_length=50, choices=yes_no_choice, null=True,  blank=True, default=None)

    lease_agreement = models.CharField(_("Lease Agreement"),max_length=50, choices=yes_no_choice , null=True, blank=True, default=None)
    contract_duration = models.CharField(_("Contract Duration"),null=True, blank=True, max_length=50)

    contract_fee = models.CharField(_("Contract Fee"),max_length=100 , null=True, blank=True)
    residual_rent = models.CharField(_("Residual Rent"),max_length=100 , null=True, blank=True)
    need_transfer_user = models.CharField(_("Need Transfer User"),max_length=50, choices=yes_no_choice, null=True,  blank=True, default=None)

    reclamation_activities = models.CharField(_("Reclamation Activities"),max_length=50, choices=yes_no_choice, null=True, blank=True, default=None)
    reclamation_intervention_type = models.ForeignKey(ReclamationInterventionType,verbose_name=_("Reclamation Intervention Type"),  on_delete=models.PROTECT, null=True, blank=True)

    reclamation_cost = models.CharField(_("Reclamation Cost"),max_length=50, null=True, blank=True)

    email = models.EmailField(blank=True)

    origin = models.CharField(max_length=10, default='admin')

    class Meta:
        verbose_name = _('Litigation')
        verbose_name_plural = _('Litigations')

