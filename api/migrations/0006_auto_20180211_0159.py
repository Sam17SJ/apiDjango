# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-11 07:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20180208_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.IntegerField()),
                ('fechaInicio', models.DateField()),
                ('acuerdo', models.IntegerField()),
                ('broker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Broker')),
            ],
        ),
        migrations.AddField(
            model_name='propiedad',
            name='descripcio',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contrato',
            name='propiedad',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Propiedad'),
        ),
    ]
