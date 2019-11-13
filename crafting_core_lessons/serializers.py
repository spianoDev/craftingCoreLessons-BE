from rest_framework import serializers
from .models import Standard, Lesson

class StandardSerializer(serializers.ModelSerializer):
    standard_url = serializers.ModelSerializer.serializer_url_field(
        view_name='standard_detail'
    )

    class Meta:
        model = Standard
        fields = ['id', 'pk', 'standard_url', 'heading', 'anchor_standard_number', 'anchor_standard_text', 'grade',
        'standard_title', 'standard_text',]

