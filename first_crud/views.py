from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .models import *


class SchoolApiView(APIView):

    def get(self, request, id=None):
        if id:
            sch_objs = School.objects.get(id=id)
        else:
            sch_objs = School.objects.all()

        data = None
        if sch_objs:
            many_value = False if id else True
            data = SchoolSerializer(sch_objs, many=many_value).data

        return Response(data)

    def post(self, request):
        if request.data:
            name = request.data.get('name')
            state = request.data.get('state')
            village = request.data.get('village')
            if name and state and village:
                school = School(
                    name=name,
                    state=state,
                    village=village
                )
                school.save()
                data = SchoolSerializer(school).data

                return Response({"success": data})
            else:
                raise serializers.ValidationError("Incomplete data")

        else:
            return Response({"error": "Invalid Request"})

    def put(self, request, id=None):
        if not id:
            raise serializers.ValidationError("instance Id is required")
        name = request.data.get('name')
        state = request.data.get('state')
        village = request.data.get('village')
        # print("YEs put method is call",request.data)
        if name and state and village:
            school = School.objects.get(id=id)
            if not school:
                raise serializers.ValidationError("School object not found")
            school.name = name
            school.state = state
            school.village = village
            school.save()
            data = SchoolSerializer(school, many=False).data
            return Response({"success": data})
        else:
            raise serializers.ValidationError("Incomplete data use the patch method")

    def delete(self, request, id=None):
        if not id:
            raise serializers.ValidationError("Instance Id  is Required")
        school = School.objects.filter(id=id).first()
        if not school:
            raise serializers.ValidationError("Instance data not found")
        # school.delete()
        return Response({"data": "School Deleted success fully"})


class StudentAPIView(APIView):
    def get(self, request, id=None):
        student = Student.objects.all()
        manyvalue = True
        if id:
            student = student.filter(id=id)
            manyvalue = False

        if not student:
            raise serializers.ValidationError("Student data was not found")
        student_data = StudentSerializers(student, many=manyvalue).data
        return Response({"data": student_data})

    def post(self, request):
        school = request.data.get('school')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        age = request.data.get('age')

        req_data = (school and first_name and last_name and age)
        if not req_data:
            raise serializers.ValidationError("data is incomplete")
        school_obj = School.objects.filter(id=school).first()
        if not school_obj:
            raise serializers.ValidationError("School data not found")

        std_obj = Student(
            school=school_obj,
            first_name=first_name,
            last_name=last_name,
            age=age
        )
        std_obj.save()
        std_data = StudentSerializers(std_obj, many=False).data
        return Response({"data": std_data})

    def put(self, request, id=None):
        if not id:
            raise serializers.ValidationError("Id is required")
        school = request.data.get('school')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        age = request.data.get('age')
        req_data = (school and first_name and last_name and age)
        if not req_data:
            raise serializers.ValidationError("data is incomplete")

        school_obj = School.objects.filter(id=school).first()
        if not school_obj:
            raise serializers.ValidationError("School data not found")

        std_obj = Student.objects.filter(id=id).first()
        if not school_obj:
            raise serializers.ValidationError("Student data not found")
        std_obj.first_name = first_name
        std_obj.last_name = last_name
        std_obj.age = age
        std_obj.school = school_obj
        std_obj.save()

        std_data = StudentSerializers(std_obj).data
        return Response({"data": std_data})

    def delete(self, reques, id=None):
        if not id:
            raise serializers.ValidationError("Instance Id  is Required")
        std = Student.objects.filter(id=id).first()
        if not std:
            raise serializers.ValidationError("Instance data not found")
        std.delete()
        return Response({"data": "student Deleted success fully"})
