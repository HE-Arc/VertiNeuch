from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lessons:detail', args=[str(self.id)])
