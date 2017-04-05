# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    last_name = models.CharField(_('Last name of User'), blank=True, max_length=255)
    first_name = models.CharField(_('First name of User'), blank=True, max_length=255)
    avatar = ProcessedImageField(upload_to='avatars',
                                 processors=[ResizeToFill(100, 100)],
                                 format='JPEG',
                                 options={'quality': 60},
                                 default='default.jpg')
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

