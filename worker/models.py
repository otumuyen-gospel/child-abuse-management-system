from django.db import models
from person.models import Person
from contact.models import Contact
from agency.models import Agency
from django.utils import timezone
from auditlog.registry import auditlog

# Create your models here.
class Worker(models.Model):
    personId = models.ForeignKey(Person, on_delete=models.CASCADE, blank=False)
    AgencyId = models.ForeignKey(Agency, on_delete=models.CASCADE, blank=False)
    contactId = models.ForeignKey(Contact, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ('personId__id',)
    def __str__(self):
        return f'{self.personId.lastName} {self.personId.firstName}'

auditlog.register(Worker)