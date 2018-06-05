# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payu', '0003_auto_20160818_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='nonseamlesstransaction',
            name='service_provider',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='address1',
            field=models.CharField(max_length=48, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='address2',
            field=models.CharField(max_length=48, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='amount',
            field=models.DecimalField(blank=True, null=True, max_digits=12, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='basket',
            field=models.CharField(max_length=12, blank=True, null=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='city',
            field=models.CharField(max_length=32, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='country',
            field=models.CharField(max_length=32, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='currency',
            field=models.CharField(max_length=8, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='custom_note',
            field=models.CharField(max_length=128, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='drop_category',
            field=models.CharField(max_length=32, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='email',
            field=models.EmailField(max_length=254, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='error_code',
            field=models.CharField(max_length=32, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='error_message',
            field=models.CharField(max_length=128, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='firstname',
            field=models.CharField(max_length=32, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='lastname',
            field=models.CharField(max_length=32, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='note_category',
            field=models.CharField(max_length=32, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='offer_key',
            field=models.CharField(max_length=32, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='orderid',
            field=models.CharField(max_length=32, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='phone',
            field=models.CharField(max_length=12, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='productinfo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='raw_request',
            field=models.TextField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='raw_response',
            field=models.TextField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='response',
            field=models.CharField(max_length=2, blank=True, null=True, choices=[('N', 'New'), ('W', 'Awaiting Confirmation'), ('S', 'Success'), ('F', 'Failure'), ('C', 'Cancelled')]),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='state',
            field=models.CharField(max_length=32, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nonseamlesstransaction',
            name='zipcode',
            field=models.CharField(max_length=8, blank=True, null=True),
        ),
    ]
