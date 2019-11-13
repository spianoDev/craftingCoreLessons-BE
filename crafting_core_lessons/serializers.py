from rest_framework import serializers
from .models import Standard, Lesson

class StandardSerializer(serializers.HyperlinkedModelSerializer):
#     standard = serializers.HyperlinkedRelatedField(
#         view_name='standard_detail',
#         read_only=True
#     )
#     standard_url = serializers.ModelSerializer.serializer_url_field(
#             view_name='standard_detail'
#         )

    class Meta:
        model = Standard
        fields = ['pk', 'heading', 'anchor_standard_number', 'anchor_standard_text', 'grade',
        'standard_title', 'standard_text',]

class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'grade', 'topic', 'materials', 'vocab', 'description', 'activities',
        'accommodations', 'standard_title',]
