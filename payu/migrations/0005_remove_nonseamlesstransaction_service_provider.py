# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payu', '0004_auto_20180223_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nonseamlesstransaction',
            name='service_provider',
        ),
    ]
