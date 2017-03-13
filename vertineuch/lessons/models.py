from django.core.urlresolvers import reverse
from django.db import models

from vertineuch.users.models import User


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(User)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lessons:detail', args=[str(self.id)])
