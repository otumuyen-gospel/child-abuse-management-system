from django.db import models
from django.utils import timezone
from auditlog.registry import auditlog

# Create your models here.
class Person(models.Model):
    firstName = models.TextField(blank=False)
    lastName = models.TextField(blank=False)
    middleName = models.TextField(blank=False)
    maidenName = models.TextField(blank=False)
    dob = models.DateField(blank=False)
    phone = models.CharField(blank=False, max_length=11)
    email = models.EmailField(blank=False)
    entranceDate = models.DateTimeField(blank=False)
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_OTHERS = 'O'
    USERS_GENDER = [
        (GENDER_MALE,'male'),
        (GENDER_FEMALE, 'female'),
        (GENDER_OTHERS, 'others'),
    ]
    gender = models.CharField(choices=USERS_GENDER,
                               default=GENDER_MALE)

    class Meta:
        ordering = ('firstName','lastName',)
    def __str__(self):
        return f'{self.lastName} {self.firstName}'
    @property
    def age(self):
        today = timezone.now().date()
        age = today.year - self.dob.year
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1 #is not yet birthday so subtract 1 from age
        return age
    

auditlog.register(Person)