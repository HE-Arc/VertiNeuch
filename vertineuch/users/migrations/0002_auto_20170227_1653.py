# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 15:53
from __future__ import unicode_literals

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(default='default.jpg', upload_to='avatars'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='First name of User'),
        ),
    ]
