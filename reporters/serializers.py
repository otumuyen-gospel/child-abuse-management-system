from rest_framework import serializers
from .models import Reporter

class ReporterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reporter
        fields = "__all__"