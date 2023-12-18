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