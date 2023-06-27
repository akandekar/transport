# Generated by Django 3.1.13 on 2022-08-12 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport_management', '0019_auto_20220805_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='diesel',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='driver_expense',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='fastag',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='miscellaneous',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='uncertainty',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
