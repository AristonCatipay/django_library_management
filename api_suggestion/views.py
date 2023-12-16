from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from suggestion.models import Suggestion
from .serializers import SuggestionSerializer
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_suggestion(request):
    suggestion = Suggestion.objects.all()
    serializer = SuggestionSerializer(suggestion, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_suggestion(request):
    serializer = SuggestionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def delete_suggestion(request, pk):
    try:
        suggestion = Suggestion.objects.get(pk=pk)
    except Suggestion.DoesNotExist:
        return Response(status=404)

    suggestion.delete()
    return Response(status=204)
