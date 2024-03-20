from django.shortcuts import render
# from rest_framework.response import Response
from rest_framework import status
# from rest_framework.decorators import api_view,APIView
from .models import Book 
from rest_framework import generics
from .serializers import BookSerializer
# Create your views here.


class BookView(generics.ListCreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

