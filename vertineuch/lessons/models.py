from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models


class Lesson(models.Model):

    RECURRENCE_CHOICES = (
        (0, 'Une fois'),
        (1, 'Tous les jours'),
        (7, 'Toute les semaines'),
        (14, 'Toute les deux semaines')
    )

    DIFFICULTY_CHOICES = (
        (0, 'Debutant'),
        (1, 'Intermediaire'),
        (2, 'Experimenté')
    )

    ACTIVITY_CHOICES = (
        (0, 'Cascade de glace'),
        (1, 'Escalade'),
        (2, 'Freeride'),
        (3, 'Haute montagne'),
        (4, 'Rando raquette'),
        (5, 'Rando ski'),
        (6, 'Via ferrata')
    )

    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='teacher')

    name = models.CharField('Nom', max_length=255)
    description = models.CharField('Description', max_length=1024, blank=True)

    start_date = models.DateField('Date du premier cours')
    end_date = models.DateField('Date du dernier cours')
    time = models.TimeField('Heure du cours')
    frequency = models.IntegerField('Fréquence', choices=RECURRENCE_CHOICES)
    difficulty = models.IntegerField('Difficulté', choices=DIFFICULTY_CHOICES)
    activity = models.IntegerField('Activité', choices=ACTIVITY_CHOICES)
    price = models.DecimalField('Prix', max_digits=6, decimal_places=2)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lessons:detail', args=[str(self.id)])
