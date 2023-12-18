from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from core.permissions import IsStaffOrReadOnly
from thesis.models import Thesis, Author, Author_List
from .serializers import ThesisSerializer, AuthorSerializer, AuthorListSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsStaffOrReadOnly])
def read_thesis(request):
    thesis = Thesis.objects.all()
    serializer = ThesisSerializer(thesis, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsStaffOrReadOnly])
def create_thesis(request):
    serializer = ThesisSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsStaffOrReadOnly])
def read_author(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsStaffOrReadOnly])
def read_author_list(request):
    author_list = Author_List.objects.all()
    serializer = AuthorListSerializer(author_list, many=True)
    return Response(serializer.data)