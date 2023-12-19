from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from borrow_book.models import Borrow_Book
from .serializers import BorrowBookSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_borrow_book(request):
    borrow_book = Borrow_Book.objects.all()
    serializer = BorrowBookSerializer(borrow_book, many=True)
    return Response(serializer.data)

