from django.urls import path
from .views import ListCreateStudent, UpdateDeleteStudent

urlpatterns = [
    path('students/', ListCreateStudent.as_view(), name='student-list-create'),
    # path('students/<int:pk>/', UpdateDeleteStudent.as_view(), name='student-update-delete'),
]
