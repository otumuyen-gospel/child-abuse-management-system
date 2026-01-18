from django.db import models
from django.utils import timezone
from auditlog.registry import auditlog

# Create your models here.
class Abuse(models.Model):
    type = models.TextField(blank=False)
    description = models.TextField(blank=False)

    class Meta:
        ordering = ('type',)
    def __str__(self):
        return f'{self.type}'

auditlog.register(Abuse)