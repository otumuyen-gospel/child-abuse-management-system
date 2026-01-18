from rest_framework import serializers
from .models import Case

class CaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = "__all__"