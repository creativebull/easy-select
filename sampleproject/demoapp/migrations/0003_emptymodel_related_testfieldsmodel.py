# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 00:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_remove_note_mood'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmptyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Related',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TestFieldsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_field', models.IntegerField(choices=[(0, b'Zero'), (1, b'One')])),
                ('text', models.TextField()),
                ('fk_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='demoapp.Related')),
                ('m2m_field', models.ManyToManyField(related_name='_testfieldsmodel_m2m_field_+', to='demoapp.Related')),
            ],
        ),
    ]