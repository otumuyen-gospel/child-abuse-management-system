from rest_framework import serializers
from .models import Perpetrator

class PerpetratorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Perpetrator
        fields = "__all__"