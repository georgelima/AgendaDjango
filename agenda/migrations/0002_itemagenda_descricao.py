# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-22 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemagenda',
            name='descricao',
            field=models.TextField(blank=True),
        ),
    ]
