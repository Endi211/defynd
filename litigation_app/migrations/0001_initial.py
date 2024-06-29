# Generated by Django 4.0.3 on 2022-08-02 13:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('configurations', '0001_initial'),
        ('lawyers_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Litigation',
            fields=[
                ('litigation_code', models.AutoField(primary_key=True, serialize=False)),
                ('is_closed', models.BooleanField(default=None, verbose_name='Closed')),
                ('value_list', models.CharField(blank=True, choices=[('25%', '25%'), ('50%', '50%'), ('75%', '75%'), ('90%', '90%'), ('100%', '100%')], max_length=10, null=True)),
                ('hyperlink_to_economics_sheet', models.CharField(blank=True, max_length=50, null=True)),
                ('upload_contract', models.FileField(blank=True, null=True, upload_to='')),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('reference', models.CharField(blank=True, max_length=50, null=True)),
                ('reception_act', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default=None, max_length=50, null=True)),
                ('date_receipt_act', models.CharField(blank=True, max_length=50, null=True)),
                ('purchase_contract', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default=None, max_length=50, null=True)),
                ('contract_date', models.CharField(blank=True, max_length=50, null=True)),
                ('starting_date', models.DateField(blank=True, null=True)),
                ('target_date', models.DateField(blank=True, null=True)),
                ('closing_date', models.CharField(blank=True, max_length=20, null=True)),
                ('initial_estimation_value', models.CharField(blank=True, max_length=50, null=True)),
                ('target_value', models.CharField(blank=True, max_length=50, null=True)),
                ('final_value', models.CharField(blank=True, max_length=50, null=True)),
                ('revenue', models.CharField(blank=True, max_length=50, null=True)),
                ('total_cost', models.CharField(blank=True, max_length=50, null=True)),
                ('EBIT', models.CharField(blank=True, max_length=50, null=True)),
                ('EBIt_percentage', models.CharField(blank=True, max_length=50, null=True)),
                ('fee_percentuale', models.CharField(blank=True, max_length=50, null=True)),
                ('registration_type', models.CharField(choices=[('Esproprio Agricolo', 'Agricultural Export'), ('Esproprio Residenziale Libera', 'Expropriation Residential Industrial Building'), ('Esproprio Industriale Libera', 'Expropriation Residential Industrial Building'), ('Esproprio Fabbricato Residenziale', 'Esproprio Fabbricato Residenziale'), ('Esproprio Fabbricato Industriale', 'Esproprio Fabbricato Industriale'), ('Area boschiva', 'Area boschiva'), ('Area industriale con fabbricati', 'Area industriale con fabbricati'), ('Area industriale senza fabbricati', 'Area industriale senza fabbricati'), ('Area Residenziale con fabbricati', 'Area Residenziale con fabbricati'), ('Area Residenziale senza fabbricati', 'Area Residenziale senza fabbricati'), ('Area Agricola con fabbricati', 'Area Agricola con fabbricati'), ('Area Agricola senza fabbricati', 'Area Agricola senza fabbricati')], default='Agricultural Export', max_length=50)),
                ('prejudicial_registrations', models.CharField(blank=True, max_length=50, null=True)),
                ('enrollment_amount', models.CharField(blank=True, max_length=50, null=True)),
                ('surface_directly_concerned', models.CharField(blank=True, max_length=50, null=True)),
                ('occupied_area', models.CharField(blank=True, max_length=50, null=True)),
                ('residual_surface', models.BigIntegerField(blank=True, null=True)),
                ('area_address', models.CharField(blank=True, max_length=50, null=True)),
                ('technical_reference', models.CharField(blank=True, max_length=50, null=True)),
                ('above_ground_quantification', models.CharField(blank=True, max_length=50, null=True)),
                ('fruit_pendants', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default=None, max_length=50, null=True)),
                ('cultivator_type', models.CharField(choices=[('Value 1', 'Value 1'), ('Value 2', 'Value 2')], default='Value 1', max_length=50)),
                ('batch_disfiguration', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default=None, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('social_economic_reform', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default=None, max_length=50, null=True)),
                ('transformation_coefficient', models.CharField(blank=True, max_length=100, null=True)),
                ('IMU_final_declaration', models.CharField(blank=True, max_length=100, null=True)),
                ('epoch_construction', models.CharField(blank=True, max_length=50, null=True)),
                ('building_titles', models.TextField(blank=True, null=True)),
                ('extension_MQ', models.CharField(blank=True, max_length=100, null=True)),
                ('residual_airspace', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default=None, max_length=50, null=True)),
                ('total_demolition', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default=None, max_length=50, null=True)),
                ('partial_demolition', models.CharField(blank=True, max_length=100, null=True)),
                ('storage_state', models.CharField(blank=True, choices=[('Great', 'Great'), ('Good', 'Good'), ('Enough', 'Enough'), ('To be Restructured', 'To be Restructured')], default=None, max_length=100, null=True)),
                ('productive_activities', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default=None, max_length=50, null=True)),
                ('lease_agreement', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default=None, max_length=50, null=True)),
                ('contract_duration', models.BigIntegerField(blank=True, null=True)),
                ('contract_fee', models.CharField(blank=True, max_length=100, null=True)),
                ('residual_rent', models.CharField(blank=True, max_length=100, null=True)),
                ('need_transfer_user', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default=None, max_length=50, null=True)),
                ('reclamation_activities', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default=None, max_length=50, null=True)),
                ('reclamation_cost', models.CharField(blank=True, max_length=50, null=True)),
                ('origin', models.CharField(default='js', max_length=10)),
                ('culture_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='configurations.culturetype')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.customer')),
                ('dispute_matter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='configurations.disputematter')),
                ('dispute_object', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='configurations.disputeobject')),
                ('lawyer_reference', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='lawyers_app.lawyer')),
                ('reclamation_intervention_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='configurations.reclamationinterventiontype')),
                ('urban_destination', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='configurations.urbandestination')),
            ],
        ),
    ]
