# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 21:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='direccion',
            new_name='direccion_1',
        ),
    ]