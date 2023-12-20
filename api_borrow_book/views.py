from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Q
from core.permissions import IsStaffOrReadOnly
from book.models import Book
from borrow_book.models import Borrow_Book
from .serializers import BorrowBookSerializer, BorrowRequestApproveSerializer, BookPickUpApproveSerializer
from datetime import date

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_borrow_book_transactions(request):
    borrow_book = Borrow_Book.objects.filter(created_by=request.user)
    serializer = BorrowBookSerializer(borrow_book, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_request_to_borrow_book(request, book_primary_key):
    book = get_object_or_404(Book, pk=book_primary_key)
    is_book_borrowed = Borrow_Book.objects.filter(created_by=request.user, book=book).filter(~Q(request_status='Returned')).exists()
    if not is_book_borrowed:
        serializer = BorrowBookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response('You already borrowed this book.', status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsStaffOrReadOnly])
def read_requests_to_borrow_book(request):
    book_request = Borrow_Book.objects.filter(request_status='Request')
    serializer = BorrowBookSerializer(book_request, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsStaffOrReadOnly])
def approve_borrow_book_request(request, borrow_book_primary_key):
    borrow_book = get_object_or_404(Borrow_Book, pk=borrow_book_primary_key)
    if borrow_book.request_status == 'Request':
        serializer = BorrowRequestApproveSerializer(borrow_book, data=request.data)
        if serializer.is_valid():
            serializer.save(request_status='Approved', staff_approve=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response('Invalid request.', status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsStaffOrReadOnly])
def read_books_for_pick_up(request):
    borrow_books = Borrow_Book.objects.filter(request_status='Approved')
    serializer = BorrowBookSerializer(borrow_books, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsStaffOrReadOnly])
def approve_book_pick_up(request, borrow_book_primary_key):
    borrow_book = get_object_or_404(Borrow_Book, pk=borrow_book_primary_key)
    if borrow_book.request_status == 'Approved':
        serializer = BookPickUpApproveSerializer(borrow_book, data=request.data)
        if serializer.is_valid():
            serializer.save(request_status='Borrowed', staff_borrow=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
    return Response('Invalid request.', status=status.HTTP_404_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsStaffOrReadOnly])
def read_books_for_return(request):
    borrow_books = Borrow_Book.objects.filter(created_by=request.user).filter(request_status='Borrowed')
    serializer = BorrowBookSerializer(borrow_books, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsStaffOrReadOnly])
def return_book(request, borrow_book_primary_key):
    borrow_book = get_object_or_404(Borrow_Book, pk=borrow_book_primary_key)
    if borrow_book.request_status == 'Borrowed':
        borrow_book.request_status = 'Returned'
        borrow_book.staff_return = request.user
        borrow_book.returned_date = date.today()

        delta = borrow_book.returned_date - borrow_book.return_due_date
        if delta.days > 0:
            borrow_book.pending_days = delta.days
            borrow_book.fine = borrow_book.pending_days * 20
        else:
            borrow_book.pending_days = 0
            borrow_book.fine = 0

        borrow_book.save()
        return Response({'message': 'Book returned successfully.'})
    else:
        return Response({'message': 'Invalid Request.'}, status=status.HTTP_404_BAD_REQUEST)
        

    
