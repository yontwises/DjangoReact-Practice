from django.shortcuts import render
from .models import Room
from rest_framework import generics
from .serializers import RoomSerializer
# Create your views here.

class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
