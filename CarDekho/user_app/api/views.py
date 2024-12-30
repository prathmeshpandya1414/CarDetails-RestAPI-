from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from user_app import models
from user_app.api.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=200)

@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered new user.'
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.errors
        return Response(data)