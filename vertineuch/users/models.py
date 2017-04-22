# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from vertineuch.lessons.models import Lesson


class User(AbstractUser):
    last_name = models.CharField(_('Nom'), blank=True, max_length=255)
    first_name = models.CharField(_('Prénom'), blank=True, max_length=255)

    # XXX cette regex ressemble à un numéro étasunien.
    phone_regex = RegexValidator(regex=r'^\+?1?\d{10,13}$',
                                 message="Le numéro de téléphone doit être sous la forme '9999999999' ou '0041999999999'")
    phone_number = models.CharField(_('Téléphone'), validators=[phone_regex], blank=True, max_length=13, null=True)

    avatar = ProcessedImageField(verbose_name='Avatar',
                                 upload_to='avatars',
                                 processors=[ResizeToFill(256, 256)],
                                 format='JPEG',
                                 options={'quality': 60},
                                 default='default.jpg')
    # TODO: change this to a group ?
    is_teacher = models.BooleanField(default=False)
    subscribed_lessons = models.ManyToManyField(Lesson, related_name="subscribed_lessons")

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
