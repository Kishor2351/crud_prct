from django.db import models

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    village = models.CharField(max_length=255)

    class Meta:
        db_table = 'student_school'

    def __str__(self):
        return self.name


class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='student')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name
