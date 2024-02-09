from django.contrib.auth.models import User, auth, Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from user_profile.models import Profile
from course.models import Course
from suggestion.models import Suggestion
from .decorators import unauthenticated_user, allow_certain_groups
from book.models import Book, Author as Book_Author
from thesis.models import Thesis , Author as Thesis_Author

def home(request):
    auth.logout(request)
    return render(request, 'core/home.html', {
        'title': 'Home',
    })

@login_required
@allow_certain_groups(allowed_groups=['staff'])
def index(request):
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    # Statistics
    books_total = Book.objects.count()
    thesis_total = Thesis.objects.count()
    students_total = User.objects.filter(groups__name='student').count()
    teachers_total = User.objects.filter(groups__name='teacher').count()
    courses_total = Course.objects.count()
    suggestions_total = Suggestion.objects.count()
    book_authors_total = Book_Author.objects.count()
    thesis_authors_total = Thesis_Author.objects.count()

    return render(request, 'core/index.html', {
        'title': 'Welcome',
        'profile': profile,
        'is_staff': request.is_staff,
        'books_total': books_total,
        'thesis_total': thesis_total,
        'students_total': students_total,
        'teachers_total': teachers_total,
        'courses_total': courses_total,
        'suggestions_total': suggestions_total,
        'book_authors_total': book_authors_total,
        'thesis_authors_total': thesis_authors_total,
    })

@unauthenticated_user
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # User is authenticated.
            auth.login(request, user)
            messages.success(request, 'Login successful. Welcome back!')
            return redirect('book:index')
        else: 
            # Invalid credentials
            messages.error(request, 'Invalid credentials. Please check your username and password.')
            return redirect('core:signin')
            
    return render(request, 'core/signin.html', {
        'title': 'Sign in',
    })

@unauthenticated_user
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already taken.')
                return redirect('core:signup')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken.')
                return redirect('core:signup')
            else:
                # Create the user
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.save()
                # Log the user in using the credentials
                credentials = auth.authenticate(username=username, password=password)
                auth.login(request, credentials)
                # Create the user profile.
                user = User.objects.get(username=username)
                if Course.objects.filter(abbreviation='NS').exists():
                    course = Course.objects.get(abbreviation='NS')
                    profile = Profile.objects.create(user=user, course=course)
                    # Add user to the student group
                    group_student = Group.objects.get(name='student')
                    user.groups.add(group_student)
                    profile.save()
                    messages.success(request, 'Account created successfully! Welcome to our community.')
                    return redirect('book:index')
                else:
                    course = Course.objects.create(name='Not Specified', abbreviation='NS')
                    profile = Profile.objects.create(user=user, course=course)

                    # Add user to the student group
                    group_teacher, created_teacher = Group.objects.get_or_create(name='teacher')
                    group_student, created_student = Group.objects.get_or_create(name='student')

                    # Make sure to use group objects, not tuples
                    user.groups.add(group_student)

                    profile.save()
                    messages.success(request, 'Account created successfully! Welcome to our community.')
                    return redirect('book:index')
        else:
            messages.info(request, 'Password don\'t match')
            return redirect('core:signup')

    return render(request, 'core/signup.html', {
        'title': 'Sign up',
    })


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout successful. Have a great day!')
    return redirect('core:signin')

@login_required
@allow_certain_groups(allowed_groups=['staff'])
def users(request):
    users = User.objects.filter(is_superuser=False)

    return render(request, 'core/users.html', {
        'title': 'Users',
        'is_staff': request.is_staff,
        'users': users,
    })