from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status
from .models import customers
from .serializers import *

class customersList(APIView):

    def get(self,request):
        customers1 = customers.objects.all()
        serializer = customersSerializer(customers1,many=True)
        return  Response(serializer.data)

    def put(self,request):
        serializer = customersSerializer(customers,data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
        return  Response(serializer.data)

    



