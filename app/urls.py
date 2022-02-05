from django.urls import path
from app.views import*
urlpatterns = [
    path('student/', StudentList.as_view()),
]
