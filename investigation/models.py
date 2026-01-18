from django.db import models
from django.utils import timezone
from auditlog.registry import auditlog
from allegation.models import Allegation

# Create your models here.
class Investigation(models.Model):
    allegationId = models.ForeignKey(Allegation, on_delete=models.CASCADE, blank=False)
    safety_plan_status = models.TextField(blank=False)
    response_type = models.TextField(blank=False)
    class Meta:
        ordering = ('allegationId__id',)
    def __str__(self):
        return f'{self.response_type}'

auditlog.register(Investigation)