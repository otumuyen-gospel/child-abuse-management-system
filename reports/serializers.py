from rest_framework import serializers
from .models import Report

class ReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"