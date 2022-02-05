from django.shortcuts import render
from app.models import*
from app.serializers import*
from rest_framework import viewsets
# Create your views here.
class StudentList(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers


    
    