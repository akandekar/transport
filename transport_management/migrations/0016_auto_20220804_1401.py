# Generated by Django 3.1.13 on 2022-08-04 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport_management', '0015_auto_20220804_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pod',
            name='received_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pod',
            name='remarks',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
