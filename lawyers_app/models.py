from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Lawyer(models.Model):
    name = models.CharField(_("Name"),max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Lawyer')
        verbose_name_plural = _('Lawyers')