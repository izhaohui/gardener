# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='action_effect_span',
        ),
        migrations.AddField(
            model_name='action',
            name='action_deadline',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='action',
            name='action_value',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
