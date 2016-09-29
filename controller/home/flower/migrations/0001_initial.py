# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('action_name', models.CharField(max_length=128)),
                ('action_effect_span', models.IntegerField()),
                ('action_status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Daily',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('env_light', models.IntegerField()),
                ('env_humid', models.IntegerField()),
                ('env_raindrop', models.IntegerField()),
                ('env_temperature', models.IntegerField()),
                ('soi_humid', models.IntegerField()),
                ('soi_fatness', models.IntegerField()),
                ('soi_temperature', models.IntegerField()),
                ('valve_flow', models.IntegerField()),
                ('valve_span', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('env_light', models.IntegerField()),
                ('env_humid', models.IntegerField()),
                ('env_raindrop', models.IntegerField()),
                ('env_temperature', models.IntegerField()),
                ('soi_humid', models.IntegerField()),
                ('soi_fatness', models.IntegerField()),
                ('soi_temperature', models.IntegerField()),
                ('valve_flow', models.IntegerField()),
                ('valve_span', models.IntegerField()),
            ],
        ),
    ]
