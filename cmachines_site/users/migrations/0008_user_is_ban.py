# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-01 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_virtualmachines_hdd_disk_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_ban',
            field=models.BooleanField(default=False),
        ),
    ]