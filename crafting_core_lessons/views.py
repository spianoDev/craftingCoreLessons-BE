from django.http import JsonResponse, HttpResponseRedirect
from .models import Standard, Lesson
from rest_framework import generics, permissions, status
from .serializers import StandardSerializer, LessonSerializer, UserSerializer, UserSerializerWithToken
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect

# @api_view(['GET', 'POST'])
# def current_user(request):
#     serializer_class = UserSerializer(request.user)
#     return Response(serializer.data)
#
# class UserList(generics.ListCreateAPIView):
#     permission_classes = (permissions.AllowAny,)
#
#     def post(self, request, format=None):
#         serializer = UserSerializerWithToken(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StandardList(generics.ListCreateAPIView):
    queryset = Standard.objects.all()
    serializer_class = StandardSerializer

class StandardDetail(generics.RetrieveAPIView):
    queryset = Standard.objects.all()
    serializer_class = StandardSerializer

class LessonList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

def standard_list(request):
    standards = Standard.objects.all()
    return render(request, 'standard_list.html', {'standards': standards})

def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'lesson_list.html', {'lessons': lessons})

def lesson_detail(request, pk):
    lesson = Lesson.objects.get(id = pk)
    return render(request, 'lesson_detail.html', {'lesson': lesson})
