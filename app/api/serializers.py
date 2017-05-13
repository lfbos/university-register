from rest_framework import serializers

from app.models import University


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('name',)
