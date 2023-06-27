# Generated by Django 3.1.13 on 2022-09-16 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport_management', '0026_auto_20220916_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='diesel',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='expense',
            name='driver_expense',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='expense',
            name='fastag',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='expense',
            name='miscellaneous',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='expense',
            name='uncertainty',
            field=models.IntegerField(default=0),
        ),
    ]
