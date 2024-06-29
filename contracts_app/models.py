from django.db import models
from django.utils.translation import gettext_lazy as _
from clients.models import Customer
from django.contrib.auth.models import User


# Create your models here.


class Contract(models.Model):
    name = models.CharField(_("Name"),max_length=50, blank=True)
    date = models.DateField(_("Date"),blank=True, null=True)
    sign_date = models.DateField(_("Sign Date"),blank=True, null=True)
    client = models.ForeignKey(Customer, verbose_name=_("Client"), on_delete=models.CASCADE, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = _('Contract')
        verbose_name_plural = _('Contracts')

class Attachment(models.Model):
    contract = models.ForeignKey(Contract, verbose_name=_("Contract"), on_delete=models.CASCADE)
    creator = models.ForeignKey(User, verbose_name=_("Creator"),  on_delete=models.CASCADE)
    file = models.FileField(_("File"))

    class Meta:
        verbose_name = _('Attachment')
        verbose_name_plural = _('Attachments')
