from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from core.permissions import IsStaffOrReadOnly
from review.models import Review, Reviewed_Item
from .serializers import ReviewSerializer, ReviewedItemSerializer
from book.models import Book

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsStaffOrReadOnly])
def create_review(request, book_id):
    review_serializer = ReviewSerializer(data=request.data)
    if review_serializer.is_valid():
        review = review_serializer.save(user=request.user, profile=request.user.profile)
        
        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        review_item_data = {'book': book.id, 'review': review.id}
        reviewed_item_serializer = ReviewedItemSerializer(data=review_item_data)

        if reviewed_item_serializer.is_valid():
            reviewed_item_serializer.save()
            return Response(review_serializer.data, status=status.HTTP_201_CREATED)
        return Response(reviewed_item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(review_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



