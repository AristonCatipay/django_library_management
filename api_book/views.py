from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from django.shortcuts import get_object_or_404
from core.permissions import IsStaffOrReadOnly
from book.models import Book, Author, Author_List
from review.models import Review, Reviewed_Item
from .serializers import BookSerializer, AuthorSerializer, AuthorListSerializer, ReviewedItemSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_book(request):
    query = request.GET.get('query', '')
    books = Book.objects.all()

    if query:
        books = books.filter(Q(title__icontains=query) | Q(isbn_number__icontains=query))

    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_book_detail(request, book_primary_key):
    book = get_object_or_404(Book, pk=book_primary_key)
    authors = Author_List.objects.filter(book_id=book_primary_key)
    book_reviews = Reviewed_Item.objects.filter(book_id=book_primary_key)

    # Serialize single objects
    serialized_book = BookSerializer(book).data
    serialized_authors = [AuthorListSerializer(author).data for author in authors] 
    serialized_reviews = [ReviewedItemSerializer(review).data for review in book_reviews]

    return Response({
        'book': serialized_book,
        'authors': serialized_authors,
        'book_reviews': serialized_reviews,
    })

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsStaffOrReadOnly])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsStaffOrReadOnly])
def update_book(request, book_primary_key):
    book = get_object_or_404(Book, id=book_primary_key)
    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsStaffOrReadOnly])
def delete_book(request, book_primary_key):
    book = get_object_or_404(Book, id=book_primary_key)
    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

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

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsStaffOrReadOnly])
def read_author_list(request):
    author_list = Author_List.objects.all()
    serializer = AuthorListSerializer(author_list, many=True)
    return Response(serializer.data)