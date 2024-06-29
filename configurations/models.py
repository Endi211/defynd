from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class AreaType(models.Model):
    name = models.CharField(_("Name"),max_length=100)

    class Meta:
        verbose_name = _('Area Type')
        verbose_name_plural = _('Area Types')

    def __str__(self):
        return f'{self.name}'


class ConstraintType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Constraint Type')
        verbose_name_plural = _('Constraint Types')

class CultureType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Culture Type')
        verbose_name_plural = _('Culture Types')

class DisputeMatter(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Dispute Matter')
        verbose_name_plural = _('Dispute Matters')

class DisputeObject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Dispute Object')
        verbose_name_plural = _('Dispute Objects')

class ReclamationInterventionType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Reclamation Intervention Type')
        verbose_name_plural = _('Reclamation Intervention Types')

class UrbanDestination(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Urban Destination')
        verbose_name_plural = _('Urban Destinations')