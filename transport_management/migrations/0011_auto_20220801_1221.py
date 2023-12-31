# Generated by Django 3.1.13 on 2022-08-01 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport_management', '0010_auto_20220731_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('deliverd', 'Delivered'), ('approved', 'Approved'), ('complete', 'Complete'), ('decline', 'Decline')], default='pending', max_length=10),
        ),
    ]
