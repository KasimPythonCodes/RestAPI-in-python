from django.contrib import admin
# Register your models here.
from .models import*

@admin.register(Student)    
class AdminStudent(admin.ModelAdmin):
    list_display=['id','stuname','email']
