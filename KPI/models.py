from django.db import models
from dashboard_page.models import Statistic


# Create your models here.


class Kpi(Statistic):
    class Meta:
        proxy = True
        verbose_name = 'KPI'

        verbose_name_plural = 'KPI'