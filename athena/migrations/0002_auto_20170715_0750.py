# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-15 07:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('athena', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worksheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(max_length=300)),
                ('solutions', models.CharField(max_length=300)),
                ('levels', models.CharField(max_length=300)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='athena.Student')),
            ],
        ),
        migrations.AlterField(
            model_name='history',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='athena.Student'),
        ),
    ]
