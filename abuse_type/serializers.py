from rest_framework import serializers
from .models import Abuse

class AbuseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Abuse
        fields = "__all__"