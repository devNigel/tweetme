# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-09-15 12:17
from __future__ import unicode_literals

from django.db import migrations, models
import tweets.models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_auto_20180913_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.CharField(max_length=140, validators=[tweets.models.validate_content]),
        ),
    ]