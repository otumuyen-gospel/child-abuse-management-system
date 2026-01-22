from rest_framework import serializers
from .models import Evidence

class EvidenceSerializers(serializers.ModelSerializer):

    class Meta:
        model = Evidence
        fields = '__all__'