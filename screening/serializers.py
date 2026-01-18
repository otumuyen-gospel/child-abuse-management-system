from rest_framework import serializers
from .models import Screening

class ScreeningSerializers(serializers.ModelSerializer):
    class Meta:
        model = Screening
        fields = "__all__"