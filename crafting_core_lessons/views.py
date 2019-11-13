from django.shortcuts import render
from django.http import JsonResponse
from .models import Standard, Lesson
from rest_framework import generics
from .serializers import StandardSerializer, LessonSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class StandardList(generics.ListCreateAPIView):
    queryset = Standard.objects.all()
    serializer_class = StandardSerializer

class StandardDetail(generics.RetrieveAPIView):
    queryset = Standard.objects.all()
    serializer_class = StandardSerializer

class LessonList(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
