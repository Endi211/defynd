from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

CHOICES = (
    ('company', _('company')),
    ('individual', _('individual')),
)

GENDER = (
    ('M', _('Male')),
    ('F', _('Female'))
)

PREFIX = (
    ('+39', '+39'),
    ('+355', '+355'),
    ('+44', '+44'),
    ('+43', '+43'),
    ('+32', '+32'),
    ('+359', '+359'),
    ('+357', '+357'),
    ('+420', '+420'),
    ('+45', '+45'),
    ('+372', '+372'),
    ('+358', '+358'),
    ('+33', '+33'),
    ('+49', '+49'),
    ('+30', '+30'),
    ('+36', '+36'),
    ('+354', '+354'),
    ('+353', '+353'),
    ('+371', '+371'),
    ('+423', '+423'),
    ('+370', '+370'),
    ('+352', '+352'),
    ('+356', '+356'),
    ('+31', '+31'),
    ('+47', '+47'),
    ('+48', '+48'),
    ('+351', '+351'),
    ('+40', '+40'),
    ('+421', '+421'),
    ('+386', '+386'),
    ('+34', '+34'),
    ('+46', '+46'),
    ('+383', '+383'),
    ('+389', '+389'),
    ('+382', '+382'),
    ('+381', '+381'),
    ('+41', '+41'),
    ('+90', '+90'),
    ('+380', '+380')
)


class Customer(models.Model):
    code = models.AutoField(_('code'), primary_key=True)
    hubspot_card = models.URLField(null=True, blank=True)
    customer_type = models.CharField(_("Customer Type"),max_length=30, choices=CHOICES, default='individual')

    company_name = models.CharField(_("Company Name"),max_length=50, blank=True)
    role = models.CharField(_("Role"),max_length=100, blank=True)
    name = models.CharField(_("Name"), max_length=50, blank=True)
    last_name = models.CharField(_("Last Name"),max_length=50, blank=True)

    vat_number = models.CharField(_("Vat Number"),max_length=30, blank=True)
    fiscal_code = models.CharField(_("Fiscal Code"),max_length=30, blank=True)
    birth_place = models.CharField(_("Birth Place"),max_length=100, blank=True)
    birthday = models.CharField(_("Birthday"),max_length=10, blank=True)
    gender = models.CharField(_("Gender"),max_length=30, choices=GENDER, blank=True)

    email = models.EmailField(_("Email"),blank=True)

    phone = models.CharField('', max_length=11, blank=True)
    mobile = models.CharField(max_length=11, blank=True)
    phone_prefix = models.CharField(_('Phone'),max_length=4, choices=PREFIX, blank=False, default='+39')
    mobile_prefix = models.CharField(_('Mobile'),max_length=4, choices=PREFIX, blank=False, default='+39')

    street = models.CharField(_("Street"),max_length=50, blank=True)
    city = models.CharField(_("City"),max_length=50, blank=True)
    post_number = models.CharField(_("Post Number"),max_length=50, blank=True)
    is_customer = models.BooleanField(_("Customer"), default=False)
    origin = models.CharField(max_length=10, default='admin')
    is_active = models.BooleanField("is Active", default=False)

    def __str__(self):
        return f'[{self.code}] {self.name}'

    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customers')