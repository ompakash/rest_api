from django.http import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from api.models import *
from .serializers import StudentSerializer

# Create your views here.


class StudentAPI(APIView):
    def get(self,reqeust,pk=None,format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id =id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created Succesfull POST'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST) 

    
    def put(self,reqeust,pk,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=reqeust.data,partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated PUT'})
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated PATCH'})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})









# @api_view(['POST','GET','PUT','PATCH','DELETE'])
# def hello_world(reqeust,pk=None):
#     if reqeust.method == 'GET':
#         # id = reqeust.data.get('id')
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(id =id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu,many=True)
#         return Response(serializer.data)

#     if reqeust.method == 'POST':
#         serializer = StudentSerializer(data = reqeust.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Created Succesfull POST'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST) 

#     if reqeust.method =='PUT':
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu,data=reqeust.data,partial=False)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Updated PUT'})
#         return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

#     if reqeust.method =='PATCH':
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu,data=reqeust.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Updated PATCH'})
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#     if reqeust.method == 'DELETE':
#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()

#         return Response({'msg':'Data Deleted'})