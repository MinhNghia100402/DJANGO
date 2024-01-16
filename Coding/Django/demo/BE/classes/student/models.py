from django.db import models

class Classes(models.Model):
    id_class = models.AutoField(primary_key=True)
    name_class = models.CharField(max_length=50)

class Teachers(models.Model):
    id_teacher = models.AutoField(primary_key=True)
    name_teacher = models.CharField(max_length=50)

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    id_class = models.ForeignKey(Classes, on_delete=models.CASCADE)
    id_teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)

        