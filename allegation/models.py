from django.db import models
from django.utils import timezone
from auditlog.registry import auditlog
from abuse_type.models import Abuse
from perpetrators.models import Perpetrator
from victims.models import Victim

# Create your models here.
class Allegation(models.Model):
    perpetratorId = models.ForeignKey(Perpetrator, on_delete=models.CASCADE, blank=False)
    victimId = models.ForeignKey(Victim, on_delete=models.CASCADE, blank=False)
    abuse_typeId = models.ForeignKey(Abuse, on_delete=models.CASCADE, blank=False)
    severity_ranking = models.IntegerField(blank=False)
    DISPOSITION_code_0 = 'substantiated'
    DISPOSITION_code_1 = 'indicated'
    DISPOSITION_code_2 = 'unfounded'
    DISPOSITION_CHOICES = [
        (DISPOSITION_code_0, 'substantiated'),
        (DISPOSITION_code_1, 'indicated'),
        (DISPOSITION_code_2, 'unfounded'),
    ]
    disposiion_code = models.CharField(choices=DISPOSITION_CHOICES,
                               default=DISPOSITION_code_2)

    class Meta:
        ordering = ('abuse_typeId__id',)
    def __str__(self):
        return f'{self.perpetratorId.personId.firstName} {self.victimId.personId.lastName}'

auditlog.register(Allegation)