# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-14 22:26
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_subscribed_lessons'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message="Le numéro de téléphone doit être sous la forme '9999999999' ou '0041999999999'", regex='^\\+?1?\\d{10,13}$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='subscribed_lessons',
            field=models.ManyToManyField(related_name='subscribed_lessons', to='lessons.Lesson'),
        ),
    ]