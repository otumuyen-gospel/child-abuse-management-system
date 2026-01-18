from rest_framework import serializers
from .models import Agency

class AgencySerializers(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = '__all__'
