# Generated by Django 5.0 on 2024-01-16 08:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id_class', models.AutoField(primary_key=True, serialize=False)),
                ('name_class', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id_teacher', models.AutoField(primary_key=True, serialize=False)),
                ('name_teacher', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('id_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.classes')),
                ('id_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.teachers')),
            ],
        ),
    ]