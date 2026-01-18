from django.db import models
from django.utils import timezone
from auditlog.registry import auditlog
from case.models import Case

# Create your models here.
class Action(models.Model):
    caseId = models.ForeignKey(Case, on_delete=models.CASCADE, blank=False)
    legal_status = models.TextField(blank=False)
    attorney = models.TextField(blank=True,null=True)
    petition = models.IntegerField(blank=True, null=True)
    action = models.TextField(blank=False)
    court_action = models.TextField(blank=True, null=True)
    action_type = models.TextField(blank=False)
    
    class Meta:
        ordering = ('action_type',)
    def __str__(self):
        return f'{self.action_type}'

auditlog.register(Action)