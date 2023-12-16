from rest_framework.response import Response
from rest_framework.decorators import api_view
from suggestion.models import Suggestion
from . serializers import SuggestionSerializer

@api_view(['GET'])
def read_suggestion(request):
    suggestion =  Suggestion.objects.all()
    serializer = SuggestionSerializer(suggestion, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_suggestion(request):
    serializer = SuggestionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update_suggestion(request, pk):
    try:
        suggestion = Suggestion.objects.get(pk=pk)
    except Suggestion.DoesNotExist:
        return Response(status=404)

    serializer = SuggestionSerializer(suggestion, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_suggestion(request, pk):
    try:
        suggestion = Suggestion.objects.get(pk=pk)
    except Suggestion.DoesNotExist:
        return Response(status=404)

    suggestion.delete()
    return Response(status=204)
