from django.db import models
from person.models import Person  
from auditlog.registry import auditlog

# Create your models here.
class Contact(models.Model):
    personId = models.ForeignKey(Person,on_delete=models.CASCADE)
    phone = models.CharField(blank=False, max_length=11)
    email = models.EmailField(blank=False)
    address = models.TextField(blank=False)
    socialMedia = models.URLField(null=True, blank=True)
    state = models.TextField(blank=False)
    country = models.TextField(blank=False)
    occupation = models.TextField(null=True, blank=True)
    ethnicity = models.TextField(blank=False)
    MARRIED = 'MARRIED'
    SINGLE = 'SINGLE'
    SEPARATED = 'SEPARATED'
    MARITAL_STATUS = [
        (MARRIED, 'MARRIED'),
        (SINGLE,'SINGLE'),
        (SEPARATED,'SEPARATED'),
    ]
    marital_status = models.CharField(choices=MARITAL_STATUS,
                               default=MARRIED)
    
    class Meta:
        ordering = ('marital_status',)
    def __str__(self):
        return f'{self.personId.firstName} {self.personId.lastName}'
    
auditlog.register(Contact)