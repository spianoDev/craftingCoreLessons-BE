from rest_framework import serializers
from .models import Standard, Lesson
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username',]

class UserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ['token', 'username', 'password',]

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
