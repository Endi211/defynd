from django.db import models
from litigation_app.models import Litigation
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Statistic(models.Model):
    title = models.CharField(_("Title"),max_length=100)
    number = models.IntegerField(_("Number"))
    initial_value = models.CharField(_("Initial Value"),max_length=100)
    objective_value = models.CharField(_("Objective Value"),max_length=100)
    final_value = models.CharField(_("Final Value"),max_length=100)
    moltiplicatore = models.CharField(max_length=100)
    revue_value = models.CharField(_("Revue Value"),max_length=100)
    total_cost_value = models.CharField(_("Total Cost Value"),max_length=100)
    EBIT = models.CharField(max_length=100)
    EBIt_percent = models.CharField('EBIT %',max_length=100)

    class Meta:
        verbose_name = _('Statistic')
        verbose_name_plural = _('Statistics')



# type 1: all litigations
# type 2: litigations with contract and is closed
# type 4: litigations with contract but not closed
# type 4: no contract , not closed


# litigation_objects = Litigation.objects.all()
#
# type_1_stat = Statistic.objects.get(title='Contenzioni in gestione')
# type_2_stat = Statistic.objects.get(title='Contenzioni chiusi con contratto')
# type_3_stat = Statistic.objects.get(title='Contenzioni aperti (not chiusa) con contratto')
# type_4_stat = Statistic.objects.get(title='Contenzioni in trativa senza contratto')
#
# type_2_objects = []
# type_3_objects = []
# type_4_objects = []
#
# for item in litigation_objects:
#     if item.upload_contract and item.is_closed:
#         type_2_objects.append(item)
#     elif item.upload_contract and not item.is_closed:
#         type_3_objects.append(item)
#     else:
#         type_4_objects.append(item)
#
# type_1_stat.number = len(litigation_objects)
# type_2_stat.number = len(type_2_objects)
# type_3_stat.number = len(type_3_objects)
# type_4_stat.number = len(type_4_objects)
#
#
#
#
# initial_value_type_1 = 0
# objective_value_type_1 = 0
# final_value_type_1 = 0
# revenue_value_type_1 = 0
# total_cost_type_1 = 0
# ebit_type_1 = 0
# ebit_percentage_type_1 = 0
#
# for field in litigation_objects:
#
#     if field.initial_estimation_value:
#         value_stripped_1 = field.initial_estimation_value.replace(',', '')
#         initial_value_type_1 += int(value_stripped_1)
#
#     if field.target_value:
#         target_value_1_stripped = field.target_value.replace(',', '')
#         objective_value_type_1 += int(target_value_1_stripped)
#
#     if field.final_value:
#         final_value_1_stripped = field.final_value.replace(',', '')
#         final_value_type_1 += int(final_value_1_stripped)
#
#     if field.revenue:
#         revenue_value_1_stripped = field.revenue.replace(',', '')
#         revenue_value_type_1 += int(revenue_value_1_stripped)
#
#     if field.total_cost:
#         total_cost_1_stripped = field.total_cost.replace(',', '')
#         total_cost_type_1 += int(total_cost_1_stripped)
#
#     if field.EBIT:
#         ebit_type_1 += int(field.EBIT)
#
#     if field.EBIt_percentage:
#         ebit_percentage_type_1 += float(field.EBIt_percentage)
#
#
# if objective_value_type_1 and initial_value_type_1:
#     type_1_stat.moltiplicatore = f'{round(((objective_value_type_1 - initial_value_type_1) / initial_value_type_1) * 100)} %'
#
#
# type_1_stat.initial_value = f'{initial_value_type_1:,} €'
# type_1_stat.objective_value = f'{objective_value_type_1:,} €'
# type_1_stat.final_value = f'{final_value_type_1:,} €'
# type_1_stat.revue_value = f'{revenue_value_type_1:,} €'
# type_1_stat.total_cost_value = f'{total_cost_type_1:,} €'
# type_1_stat.EBIT = f'{ebit_type_1:,} €'
# type_1_stat.EBIt_percent = f'{ebit_percentage_type_1} %'
#
# type_1_stat.save()
#
#
#
# initial_value_type_2 = 0
# objective_value_type_2 = 0
# final_value_type_2 = 0
# revenue_value_type_2 = 0
# total_cost_type_2 = 0
# ebit_type_2 = 0
# ebit_percentage_type_2 = 0
#
# for field in type_2_objects:
#
#     if field.initial_estimation_value:
#         value_stripped_2 = field.initial_estimation_value.replace(',', '')
#         initial_value_type_2 += int(value_stripped_2)
#
#     if field.target_value:
#         target_value_2_stripped = field.target_value.replace(',', '')
#         objective_value_type_2 += int(target_value_2_stripped)
#
#     if field.final_value:
#         final_value_2_stripped = field.final_value.replace(',', '')
#         final_value_type_2 += int(final_value_2_stripped)
#
#     if field.revenue:
#         revenue_value_2_stripped = field.revenue.replace(',', '')
#         revenue_value_type_2 += int(revenue_value_2_stripped)
#
#     if field.total_cost:
#         total_cost_2_stripped = field.total_cost.replace(',', '')
#         total_cost_type_2 += int(total_cost_2_stripped)
#
#     if field.EBIT:
#         ebit_type_2 += int(field.EBIT)
#
#     if field.EBIt_percentage:
#         ebit_percentage_type_2 += float(field.EBIt_percentage)
#
#
# if objective_value_type_2 and initial_value_type_2:
#     type_2_stat.moltiplicatore = f'{round(((objective_value_type_2 - initial_value_type_2) / initial_value_type_2) * 100)} %'
#
# type_2_stat.initial_value = f'{initial_value_type_2:,} €'
# type_2_stat.objective_value = f'{objective_value_type_2:,} €'
# type_2_stat.final_value = f'{final_value_type_2:,} €'
# type_2_stat.revue_value = f'{revenue_value_type_2:,} €'
# type_2_stat.total_cost_value = f'{total_cost_type_2:,} €'
# type_2_stat.EBIT = f'{ebit_type_2:,} €'
# type_2_stat.EBIt_percent = f'{ebit_percentage_type_2} %'
#
# type_2_stat.save()
#
#
#
# initial_value_type_3 = 0
# objective_value_type_3 = 0
# final_value_type_3 = 0
# revenue_value_type_3 = 0
# total_cost_type_3 = 0
# ebit_type_3 = 0
# ebit_percentage_type_3 = 0
#
# for field in type_3_objects:
#
#     if field.initial_estimation_value:
#         value_stripped_3 = field.initial_estimation_value.replace(',', '')
#         initial_value_type_3 += int(value_stripped_3)
#
#     if field.target_value:
#         target_value_3_stripped = field.target_value.replace(',', '')
#         objective_value_type_3 += int(target_value_3_stripped)
#
#     if field.final_value:
#         final_value_3_stripped = field.final_value.replace(',', '')
#         final_value_type_3 += int(final_value_3_stripped)
#
#     if field.revenue:
#         revenue_value_3_stripped = field.revenue.replace(',', '')
#         revenue_value_type_3 += int(revenue_value_3_stripped)
#
#     if field.total_cost:
#         total_cost_3_stripped = field.total_cost.replace(',', '')
#         total_cost_type_3 += int(total_cost_3_stripped)
#
#     if field.EBIT:
#         ebit_type_3 += int(field.EBIT)
#
#     if field.EBIt_percentage:
#         ebit_percentage_type_3 += float(field.EBIt_percentage)
#
# if objective_value_type_3 and initial_value_type_3:
#     type_3_stat.moltiplicatore = f'{round(((objective_value_type_3 - initial_value_type_3) / initial_value_type_3) * 100)} %'
#
# type_3_stat.initial_value = f'{initial_value_type_3:,} €'
# type_3_stat.objective_value = f'{objective_value_type_3:,} €'
# type_3_stat.final_value = f'{final_value_type_3:,} €'
# type_3_stat.revue_value = f'{revenue_value_type_3:,} €'
# type_3_stat.total_cost_value = f'{total_cost_type_3:,} €'
# type_3_stat.EBIT = f'{ebit_type_3:,} €'
# type_3_stat.EBIt_percent = f'{ebit_percentage_type_3} %'
#
# type_3_stat.save()
#
#
#
# initial_value_type_4 = 0
# objective_value_type_4 = 0
# final_value_type_4 = 0
# revenue_value_type_4 = 0
# total_cost_type_4 = 0
# ebit_type_4 = 0
# ebit_percentage_type_4 = 0
#
# for field in type_4_objects:
#
#     if field.initial_estimation_value:
#         value_stripped_4 = field.initial_estimation_value.replace(',', '')
#         initial_value_type_4 += int(value_stripped_4)
#
#     if field.target_value:
#         target_value_4_stripped = field.target_value.replace(',', '')
#         objective_value_type_4 += int(target_value_4_stripped)
#
#     if field.final_value:
#         final_value_4_stripped = field.final_value.replace(',', '')
#         final_value_type_4 += int(final_value_4_stripped)
#
#     if field.revenue:
#         revenue_value_4_stripped = field.revenue.replace(',', '')
#         revenue_value_type_4 += int(revenue_value_4_stripped)
#
#     if field.total_cost:
#         total_cost_4_stripped = field.total_cost.replace(',', '')
#         total_cost_type_4 += int(total_cost_4_stripped)
#
#     if field.EBIT:
#         ebit_type_4 += int(field.EBIT)
#
#     if field.EBIt_percentage:
#         ebit_percentage_type_4 += float(field.EBIt_percentage)
#
# if objective_value_type_4 and initial_value_type_4:
#     type_4_stat.moltiplicatore = f'{round(((objective_value_type_4 - initial_value_type_4) / initial_value_type_4) * 100)} %'
#
# type_4_stat.initial_value = f'{initial_value_type_4:,} €'
# type_4_stat.objective_value = f'{objective_value_type_4:,} €'
# type_4_stat.final_value = f'{final_value_type_4:,} €'
# type_4_stat.revue_value = f'{revenue_value_type_4:,} €'
# type_4_stat.total_cost_value = f'{total_cost_type_4:,} €'
# type_4_stat.EBIT = f'{ebit_type_4:,} €'
# type_4_stat.EBIt_percent = f'{ebit_percentage_type_4} %'
#
# type_4_stat.save()



















