from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models


class Lesson(models.Model):

    RECURRENCE_CHOICES = (
        (0, 'None'),
        (1, 'Daily'),
        (7, 'Weekly'),
        (14, 'Biweekly')
    )

    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='teacher')

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024, blank=True)

    start_date = models.DateField('Date du premier cours')
    end_date = models.DateField('Date du dernier cours')
    time = models.TimeField('Heure du cours')
    frequency = models.IntegerField(choices=RECURRENCE_CHOICES)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lessons:detail', args=[str(self.id)])
