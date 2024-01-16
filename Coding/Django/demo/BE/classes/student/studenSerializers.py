from rest_framework import serializers

from . import models

class StudentSerializer(serializers.ModelSerializer):
    class stds:
        model = models.Student
        field = ('id', 'name','id_class', 'id_teacher')