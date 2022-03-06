from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from .models import Account
from .tools import Tools

import json

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def SignUp(request):
    try:
        bodyStr = request.body.decode('utf-8')
        username = json.loads(bodyStr).get('username')
        email = json.loads(bodyStr).get('email')
        password = json.loads(bodyStr).get('password')
        tools = Tools()
        errorInForm = tools.CheckUserData(username, email, password)

        if errorInForm != "":
            return Response(data={'error': errorInForm}, status=401)

        user = Account.objects.create_user(email, username, password)

        return Response(data={'success': 'user ' + user.username + ' created.'}, status=201)
    except Exception as e:
        return Response(data={'error':e.args}, status=400)

@api_view(['POST'])
@permission_classes([AllowAny])
def SignIn(request):
    try:
        bodyStr = request.body.decode('utf-8')
        username = json.loads(bodyStr).get('username')
        password = json.loads(bodyStr).get('password')

        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': 'Invalid Credentials'}, status=401)

        token, _ = Token.objects.get_or_create(user=user)

        return Response({'token': token.key}, status=200)
    except Exception as e:
        return Response(data={'error':e.args}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def SignOut(request):
    try:
        user = request.user
        Token.objects.delete(user=user)
    except Exception as e:
        return Response(data={'error':e.args}, status=400)
    return Response({'token': 'deleted'}, status=200)