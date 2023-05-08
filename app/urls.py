from django.urls import path
from app.views import*
urlpatterns = [
    path('', StudentList.as_view()),
]
