from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from book.models import Book
from .serializers import BookSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_book(request):
    query = request.GET.get('query', '')
    books = Book.objects.all()

    if query:
        books = books.filter(Q(title__icontains=query) | Q(isbn_number__icontains=query))

    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)    