from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employees
from .serializers import employeesSerializer
from rest_framework.decorators import api_view


# Create your views here.  
@api_view(['GET', 'POST', 'DELETE'])
def employees_api(request, pk=None):
  if request.method == 'GET':
    id = pk
    #id = request.data.get('id')
    if id is not None:
      emp = employees.objects.get(id=id) 
      serializer= employeesSerializer(emp)
      return Response(serializer.data)
    emp = employees.objects.all()
    serializer= employeesSerializer(emp, many= True)
    return Response(serializer.data)
  if request.method == 'POST':
    serializer= employeesSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg': 'Data Created'}) 
    return response(serializer.errors)
  if request.method == 'DELETE':
    id= pk
    emp = employees.objects.get(pk=id)
    emp.delete()
    return Response({'msg':'Data Deleted'})

class employeeList(APIView):

    def get(self,request):
        employees1= employees.objects.all()
        serializer= employeesSerializer(employees1, many= True)
        return Response(serializer.data)

    

