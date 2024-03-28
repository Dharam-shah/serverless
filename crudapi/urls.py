from django.urls import path
from .views import StudentListCreateAPIView, StudentRetrieveUpdateDeleteAPIView
from . import views

urlpatterns = [
    path('task/', StudentListCreateAPIView.as_view(), name='task-list-create'),
    path('task/<int:pk>/', StudentRetrieveUpdateDeleteAPIView.as_view(), name='task-retrieve-update-destroy'),
]