# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20170418_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='subscribed_lessons',
            field=models.ManyToManyField(related_name='subscribed_lessons', to='lessons.Lesson'),
        ),
    ]
