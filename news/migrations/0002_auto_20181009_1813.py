# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-09 15:13
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='post',
            field=tinymce.models.HTMLField(),
        ),
    ]