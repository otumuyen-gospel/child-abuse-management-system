from django.db import models
from reporters.models import Reporter
from contact.models import Contact
from django.utils import timezone
from auditlog.registry import auditlog

# Create your models here.
class Report(models.Model):
    reporterId = models.ForeignKey(Reporter, on_delete=models.CASCADE, blank=False)
    source  = models.TextField(blank=False)
    summary = models.TextField(blank=False)
    status = models.TextField(blank=False, default='New')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('reporterId__id',)
    def __str__(self):
        return f'{self.reporterId.personId.lastName} {self.reporterId.personId.firstName}'


auditlog.register(Reporter)