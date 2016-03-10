# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-08 02:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appDS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField(max_length=255)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('foto', models.ImageField(upload_to=b'')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appDS.Proveedor'),
        ),
    ]