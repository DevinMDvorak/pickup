# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='latitude',
            field=models.DecimalField(default=-94.1608, max_digits=9, decimal_places=6),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='longitude',
            field=models.DecimalField(default=-94.1608, max_digits=9, decimal_places=6),
        ),
    ]
