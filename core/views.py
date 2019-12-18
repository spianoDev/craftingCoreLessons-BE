from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken


@api_view(['GET'])
def current_user(request):

    serializer = UserSerializer(request.user)
    return Response(serializer.data)

class UserList(APIView):
    permission_classes = (permissions.AllowAny,)
#     authentication_classes = (JSONWebTokenAuthentication,)
#         permission_classes = (IsOwner,)
#     authentication_classes = (authentication.TokenAuthentication)

#     def get(self, request, format=None):
#         """
#         Returns a list of all users
#         """
#         users = [user.users for user in User.objects.all()]
#         return Response(users)

    def post(self, request):
        user = request.data
        if not user:
            return Response({'response': 'error', 'message': 'No data found'})
        serializer = UserSerializerWithToken(data=user)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response({'response': 'error', 'message': 'serializer.errors'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'response': 'success', 'message': 'login created!'}, status=status.HTTP_201_CREATED)

