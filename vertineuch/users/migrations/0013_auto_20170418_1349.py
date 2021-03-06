# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20170418_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='user',
            name='subscribed_lessons',
            field=models.ManyToManyField(related_name='subscribed_lessons', to='lessons.Lesson'),
        ),
    ]
