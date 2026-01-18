from django.db import models
from django.utils import timezone
from auditlog.registry import auditlog
from victims.models import Victim

# Create your models here.
class Service(models.Model):
    VictimId = models.ForeignKey(Victim, on_delete=models.CASCADE, blank=False)
    type = models.TextField(blank=False)
    date = models.DateField(blank=False)
    description = models.TextField(blank=False)

    class Meta:
        ordering = ('type',)
    def __str__(self):
        return f'{self.VictimId.personId.firstName} {self.VictimId.personId.lastName}'

auditlog.register(Service)