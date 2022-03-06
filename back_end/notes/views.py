from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from rest_framework.response import Response

from .models import Note
from account.models import Account
import json

# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def ApiOverview(request):
    data = {
        'api-overview/': 'GET all routes and methods',
        'notes/': 'GET all notes from a user, body : { user_id:... }',
        'notes/delete/': 'DELETE a note, body : { user_id:..., note_id:... }',
        'notes/create/': 'POST a note, body : { user_id:..., note_title:..., note_content:... }'
    }
    return Response(data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def GetAllNotes(request):
    user = request.user

    queryset = list(Note.objects.filter(author=user).values())
    return Response(queryset, status=200)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteNote(request):
    bodyStr = request.body.decode('utf-8')
    user = request.user
    noteId = json.loads(bodyStr).get('note_id')

    Note.objects.filter(id=noteId, author=user).delete()
    return Response(data={'note': 'deleted'}, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateNote(request): # TODO Body verification and data checking
    bodyStr = request.body.decode('utf-8')
    user = request.user
    noteTitle = json.loads(bodyStr).get('note_title')
    noteContent = json.loads(bodyStr).get('note_content')
    if noteTitle == "" and noteContent == "":
        return Response(data={'note': 'not created'}, status=400)

    Note.objects.create(title=noteTitle, content=noteContent, author=user)
    return Response(data={'note': 'created'}, status=201)

