from django.db import models
from reports.models import Report
from reporters.models import Reporter
from perpetrators.models import Perpetrator
from victims.models import Victim
from worker.models import Worker
from abuse_type.models import Abuse
from django.utils import timezone
from auditlog.registry import auditlog

# Create your models here.
class Case(models.Model):
    reportId = models.ForeignKey(Report, on_delete=models.CASCADE, blank=False)
    workerId = models.ForeignKey(Worker, on_delete=models.CASCADE, blank=False)
    perpetratorId = models.ForeignKey(Perpetrator, on_delete=models.CASCADE , blank=False)
    VictimId = models.ForeignKey(Victim, on_delete=models.CASCADE, blank=False)
    reporterId = models.ForeignKey(Reporter, on_delete=models.CASCADE, blank=False)
    abuseTypeId = models.ForeignKey(Abuse, on_delete=models.CASCADE, blank=False)
    startDate = models.DateField(blank=False)
    endDate = models.DateField(blank=True, null=True)
    outcome = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('startDate',)
    def __str__(self):
        return f'{self.workerId.personId.lastName} {self.workerId.personId.firstName}'

auditlog.register(Case)