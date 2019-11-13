from rest_framework import serializers
from .models import Standard, Lesson
# from .serializers import StandardSerializer, LessonSerializer

class StandardSerializer(serializers.ModelSerializer):
#     lessons = serializers.HyperlinkedRelatedField(
#         view_name='lesson_detail',
#         many=True,
#         read_only=True
#     )
#     standard_url = serializers.ModelSerializer.serializer_url_field(
#             view_name='standard_detail'
#         )

    class Meta:
        model = Standard
        fields = ['pk', 'heading', 'anchor_standard_number', 'anchor_standard_text', 'grade',
        'standard_title', 'standard_text', ]

class LessonSerializer(serializers.ModelSerializer):
#     data = serializers.PrimaryKeyRelatedField(
#         view_name='standard_detail',
#         read_only=True
#     )
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'grade', 'topic', 'materials', 'vocab', 'description', 'activities',
        'accommodations','standard_title', ]
