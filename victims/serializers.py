from rest_framework import serializers
from .models import Victim

class VictimSerializers(serializers.ModelSerializer):
    class Meta:
        model = Victim
        fields = "__all__"