from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
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

@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsStaffOrReadOnly])
def update_thesis(request, thesis_primary_key):
    thesis = get_object_or_404(Thesis, pk=thesis_primary_key)
    serializer = ThesisSerializer(thesis, data=request.data)
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

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsStaffOrReadOnly])
def create_author(request):
    serializer = AuthorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsStaffOrReadOnly])
def update_author(request, author_primary_key):
    author = get_object_or_404(Author, pk=author_primary_key)
    serializer = AuthorSerializer(author, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsStaffOrReadOnly])
def read_author_list(request):
    author_list = Author_List.objects.all()
    serializer = AuthorListSerializer(author_list, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsStaffOrReadOnly])
def create_author_list(request):
    serializer = AuthorListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsStaffOrReadOnly])
def update_author_list(request, author_list_primary_key):
    author_list = get_object_or_404(Author_List, pk=author_list_primary_key)
    serializer = AuthorListSerializer(author_list, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)