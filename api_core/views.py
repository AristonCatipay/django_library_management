from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User, auth
from core.permissions import IsStaffOrReadOnly, UnauthenticatedOnly
from .serializers import SignInSerializer, SignUpSerializer
from course.models import Course
from user_profile.models import Profile

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