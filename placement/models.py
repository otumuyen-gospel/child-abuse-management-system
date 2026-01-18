from django.db import models
from django.utils import timezone
from auditlog.registry import auditlog
from abuse_type.models import Abuse
from perpetrators.models import Perpetrator
from victims.models import Victim

# Create your models here.
class Placement(models.Model):
    resources = models.TextField(blank=False)
    provider = models.TextField(blank=False)
    license = models.TextField(blank=False)
    capacity = models.IntegerField(blank=False)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    victimId = models.ForeignKey(Victim, on_delete=models.CASCADE, blank=False)
    
    class Meta:
        ordering = ('start_date',)
    def __str__(self):
        return f'{self.provider}'

auditlog.register(Placement)