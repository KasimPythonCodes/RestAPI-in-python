from django.shortcuts import render
from app.models import*
from app.serializers import*
from rest_framework.generics import ListAPIView
# Create your views here.
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers