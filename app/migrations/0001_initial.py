# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-24 20:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Broker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=250)),
                ('numTelefonico', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estrella',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rankin', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alto', models.IntegerField()),
                ('ancho', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioGratuito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('numTelefonico', models.IntegerField()),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='broker',
            name='estrella',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Estrella'),
        ),
    ]
