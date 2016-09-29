# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0002_auto_20160830_0506'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Action',
        ),
    ]
