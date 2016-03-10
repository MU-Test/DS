# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-05 22:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0002_auto_20160305_2219'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proveedores.Proveedor'),
        ),
    ]
