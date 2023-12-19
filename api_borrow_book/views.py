from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Q
from book.models import Book
from borrow_book.models import Borrow_Book
from .serializers import BorrowBookSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_borrow_book(request):
    borrow_book = Borrow_Book.objects.filter(created_by=request.user)
    serializer = BorrowBookSerializer(borrow_book, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_borrow_book(request, book_primary_key):
    book = get_object_or_404(Book, pk=book_primary_key)
    is_book_borrowed = Borrow_Book.objects.filter(created_by=request.user, book=book).filter(~Q(request_status='Returned')).exists()
    if not is_book_borrowed:
        serializer = BorrowBookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response('You already borrowed this book.', status=status.HTTP_400_BAD_REQUEST)


