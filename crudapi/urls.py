from django.urls import path
from .views import StudentListCreateAPIView, StudentRetrieveUpdateDeleteAPIView
from . import views

urlpatterns = [
    path('student/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('student/<int:pk>/', StudentRetrieveUpdateDeleteAPIView.as_view(), name='student-retrieve-update-destroy'),
]