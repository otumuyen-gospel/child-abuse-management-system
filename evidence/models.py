from django.db import models
from reports.models import Report 
from auditlog.registry import auditlog

# Create your models here.
def upload_to(instance, filename):
    return 'user_evidence_files_{0}_{1}'.format(instance.id, filename)

class Evidence(models.Model):
    evidenceFile = models.FileField(blank=False, upload_to=upload_to)
    evidenceFile2 = models.FileField(blank=True, null=True, upload_to=upload_to)
    evidenceFile3 = models.FileField(blank=True, null=True, upload_to=upload_to)
    evidenceFile4 = models.FileField(blank=True, null=True, upload_to=upload_to)
    reportId = models.ForeignKey(Report, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.reportId.reporterId.personId.firstName}'
    
# Register with auditlog, excluding the binary field
auditlog.register(Evidence)