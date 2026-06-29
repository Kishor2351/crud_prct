from .models import *
from rest_framework import serializers


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = '__all__'


class StudentSerializers(serializers.ModelSerializer):
    school = SchoolSerializer()

    class Meta:
        model = Student
        fields = '__all__'
