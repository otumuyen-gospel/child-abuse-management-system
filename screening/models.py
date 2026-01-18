from django.db import models
from django.utils import timezone
from auditlog.registry import auditlog
from reports.models import Report

# Create your models here.
class Screening(models.Model):
    reportId = models.ForeignKey(Report, on_delete=models.CASCADE, blank=False)
    outcome = models.TextField(blank=False)
    review_team_approval = models.BooleanField(default=False)

    class Meta:
        ordering = ('reportId__id',)
    def __str__(self):
        return f'{self.reportId.reporterId.personId.firstName} {self.reportId.victimId.personId.lastName}'

auditlog.register(Screening)