# Generated by Django 4.0.3 on 2022-08-02 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='is_active'),
        ),
    ]
