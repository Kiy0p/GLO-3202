from .models import Note 

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Note
import json

# Create your views here.

@api_view(['GET'])
def ApiOverview(request):
    data = {
        'api-overview/': 'GET all routes and methods',
        'notes/': 'GET all notes from a user, body : { user_id:... }',
        'notes/delete/': 'DELETE a note, body : { user_id:..., note_id:... }',
        'notes/create/': 'POST a note, body : { user_id:..., note_title:..., note_content:... }'
    }
    return Response(data)

@api_view(['POST'])
def GetAllNotes(request):
    bodyStr = request.body.decode('utf-8')
    userId = json.loads(bodyStr).get('user_id')

    queryset = list(Note.objects.filter(author=userId).values())
    return Response(queryset)

@api_view(['DELETE'])
def DeleteNote(request):
    bodyStr = request.body.decode('utf-8')
    userId = json.loads(bodyStr).get('user_id')
    noteId = json.loads(bodyStr).get('note_id')

    Note.objects.filter(id=noteId, author=userId).delete()
    return Response({'note': 'deleted'})

@api_view(['POST'])
def CreateNote(request): # TODO Body verification and data checking
    bodyStr = request.body.decode('utf-8')
    userId = json.loads(bodyStr).get('user_id')
    noteTitle = json.loads(bodyStr).get('note_title')
    noteContent = json.loads(bodyStr).get('note_content')
    if noteTitle == "" and noteContent == "":
        return Response({'note': 'not created'})

    Note.objects.create(title=noteTitle, content=noteContent, author=userId)
    return Response({'note': 'created'})

