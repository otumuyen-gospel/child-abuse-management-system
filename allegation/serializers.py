from rest_framework import serializers
from .models import Allegation

class AllegationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allegation
        fields = "__all__"