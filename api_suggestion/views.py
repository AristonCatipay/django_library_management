from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from suggestion.models import Suggestion
from .serializers import SuggestionSerializer

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
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Check if the logged-in user is the creator of the suggestion
    if request.user != suggestion.created_by:
        return Response("You don't have permission to perform this action.", status=status.HTTP_403_FORBIDDEN)

    serializer = SuggestionSerializer(suggestion, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_suggestion(request, pk):
    try:
        suggestion = Suggestion.objects.get(pk=pk)
    except Suggestion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Check if the logged-in user is the creator of the suggestion
    if request.user != suggestion.created_by:
        return Response("You don't have permission to perform this action.", status=status.HTTP_403_FORBIDDEN)

    suggestion.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
