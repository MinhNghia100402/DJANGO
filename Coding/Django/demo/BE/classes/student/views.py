from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework import status
from student.models import Student
from student.models import Classes
from student.models import Teachers
from django.shortcuts import get_object_or_404

from student.studenSerializers import StudentSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class ListCreateStudent(ListCreateAPIView):
    model = Student #dinh nghia model
    Serializers_student = StudentSerializer # dinh nghia lop anh xa cua model

    def get_queryset(self):
        return Student.objects.all()
    
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return JsonResponse(
            {'message': 'create successfully'},
            status=status.HTTP_201_CREATED,
        )
    
    

class UpdateDeleteStudent(RetrieveUpdateDestroyAPIView):
    model  = Student
    serializes = StudentSerializer
    def put(self, request, *args, **kwargs):
        student = get_object_or_404(student, id=kwargs.get('pk'))
        serializes = StudentSerializer(student, data = request.data)
        if serializes.is_valid():
            serializes.save()
            return JsonResponse(
                {'message': 'updated successfully'},
                status = status.HTTP_200_OK
            )
        return JsonResponse(
            {'message': 'update failed'},
            status = status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self,request,*args,**kwargs):
        student = get_object_or_404(student,id=kwargs.get('pk'))
        student.delete()

        return JsonResponse({
            'message':'Delete successful'
        },status= status.HTTP_200_OK
        )
