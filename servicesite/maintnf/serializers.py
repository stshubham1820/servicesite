from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import contact_us
class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = contact_us
        fields = '__all__'