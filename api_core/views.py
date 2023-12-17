from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User, auth
from core.permissions import IsStaffOrReadOnly, UnauthenticatedOnly
from .serializers import SignUpSerializer, UserSerializer
from course.models import Course
from user_profile.models import Profile
from suggestion.models import Suggestion
from book.models import Book, Author as Book_Author
from thesis.models import Thesis , Author as Thesis_Author

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_statistics(request):
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    books_total = Book.objects.count()
    thesis_total = Thesis.objects.count()
    students_total = User.objects.filter(groups__name='student').count()
    teachers_total = User.objects.filter(groups__name='teacher').count()
    courses_total = Course.objects.count()
    suggestions_total = Suggestion.objects.count()
    book_authors_total = Book_Author.objects.count()
    thesis_authors_total = Thesis_Author.objects.count()

    data = {
        'profile': {
            'id': profile.id,
            'image': profile.image.url,
            'gender': profile.gender,
            'student_number': profile.student_number,
            'student_contact_no': profile.student_contact_no,
        },
        'statistics': {
            'books_total': books_total,
            'thesis_total': thesis_total,
            'students_total': students_total,
            'teachers_total': teachers_total,
            'courses_total': courses_total,
            'suggestions_total': suggestions_total,
            'book_authors_total': book_authors_total,
            'thesis_authors_total': thesis_authors_total,
        }
    }

    return Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([UnauthenticatedOnly])
def signup(request):
    signup_serializer = SignUpSerializer(data=request.data)
    
    if signup_serializer.is_valid():
        validated_data = signup_serializer.validated_data
        email = validated_data['email']
        username = validated_data['username']
        
        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email is already taken'}, status=status.HTTP_400_BAD_REQUEST)
        elif User.objects.filter(username=username).exists():
            return Response({'error': 'Username is already taken'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = User.objects.create_user(**validated_data)
            
            # Creating the profile for the user
            course = Course.objects.get(abbreviation='NS')
            profile = Profile.objects.create(user=user, course=course)
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    else:
        return Response(signup_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@permission_classes([UnauthenticatedOnly])
def signin(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = auth.authenticate(username=username, password=password)
    if user is not None:
        # User is authenticated.
        auth.login(request, user)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        # Invalid credentials
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsStaffOrReadOnly])
def read_user(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)
