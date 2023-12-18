from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from book.models import Book
from .serializers import BookSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_book(request):
    book = Book.objects.all()
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)