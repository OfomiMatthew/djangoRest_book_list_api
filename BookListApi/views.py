from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,APIView
# Create your views here.

class Books(APIView):
  def get(self,request):
    author = request.GET.get('name')
    if author:
      return Response({"message":"Author name is " + author}, status=status.HTTP_200_OK)
    return Response({"name":"Things fall apart"})
  def put(self,request):
    return Response("hola")
  def post(self,request):
    return Response({"title":request.data.get('title'),"isbn":request.data.get('isbn')})

class Book(APIView):
  def get(self,request,id):
    return Response({"message":"Book with id number of " + str(id)})
  