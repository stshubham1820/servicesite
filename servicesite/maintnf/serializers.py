from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import *
class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = contact_us
        fields = '__all__'

class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model = about_us
        fields = '__all__'

class Service_categorySerializers(serializers.ModelSerializer):
    class Meta:
        model = service_category
        fields = '__all__'

class Service_sub_categorySerializers(serializers.ModelSerializer):
    class Meta:
        model = service_sub_category
        fields = '__all__'

class TestimonialsSerializers(serializers.ModelSerializer):
    class Meta:
        model = testimonials
        fields = '__all__'

class FeedbackSerializers(serializers.ModelSerializer):
    class Meta:
        model = feedback
        fields = '__all__'

class TeamSerializers(serializers.ModelSerializer):
    class Meta:
        model = team
        fields = '__all__'