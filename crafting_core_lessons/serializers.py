from rest_framework import serializers
from .models import Standard, Lesson


class StandardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Standard
        fields = ['pk', 'heading', 'anchor_standard_number', 'anchor_standard_text', 'grade',
        'standard_title', 'standard_text', ]

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['id', 'name', 'grade', 'topic', 'materials', 'vocab', 'description', 'activities',
        'accommodations','standard_title', ]
