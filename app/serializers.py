from rest_framework import serializers
from .models import*
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['stuname','email']