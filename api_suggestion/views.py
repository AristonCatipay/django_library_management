from rest_framework.response import Response
from rest_framework.decorators import api_view
from suggestion.models import Suggestion
from . serializers import SuggestionSerializer

@api_view(['GET'])
def getData(request):
    suggestion =  Suggestion.objects.all()
    serializer = SuggestionSerializer(suggestion, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_suggestion(request):
    serializer = SuggestionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)