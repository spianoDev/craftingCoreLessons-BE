from django.http import JsonResponse, HttpResponseRedirect
from .models import Standard, Lesson
from rest_framework import generics, permissions
from .serializers import StandardSerializer, LessonSerializer
from django.shortcuts import render, redirect
from .forms import LessonForm


class StandardList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Standard.objects.all()
    serializer_class = StandardSerializer

class StandardDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Standard.objects.all()
    serializer_class = StandardSerializer

class LessonList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny,)
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

def lesson_create(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            return redirect('lesson_detail', pk=lesson.pk)
    else:
        form = LessonForm()
    return render(request, 'lesson_form.html', {'form': form})

def lesson_edit(request, pk):
    lesson = Lesson.objects.get(pk=pk)
    if request.method == "POST":
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            lesson = form.save()
            return redirect('lesson_detail', pk=lesson.pk)
    else:
        form = LessonForm(instance=lesson)
    return render(request, 'lesson_form.html', {'form': form})

def lesson_delete(request, pk):
    Lesson.objects.get(id=pk).delete()
    return redirect('lesson_list')
