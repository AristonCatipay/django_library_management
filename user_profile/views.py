from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages

from . models import Profile

User = get_user_model()

def index(request):
    is_staff = True if request.user.groups.filter(name='staff') else False

    return render(request, 'user_profile/index.html', {
        'title': 'Profile',
        'is_staff': is_staff,
    })

def edit(request):
    is_staff = True if request.user.groups.filter(name='staff') else False

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        student_number = request.POST['student_number'] 
        student_contact_no = request.POST['student_contact_no']

        if request.FILES.get('image') == None:
            # If the user didn't upload their own image
            # Use the default profile image.

            image = request.user.profile.image

            # Update profile model
            request.user.profile.image = image
            request.user.profile.student_number = student_number
            request.user.profile.student_contact_no = student_contact_no
            request.user.profile.save()

            # Updated the user model 
            request.user.first_name = first_name
            request.user.last_name = last_name
            request.user.username = username
            request.user.email = email
            request.user.save()

        if request.FILES.get('image') != None:
            image = request.FILES.get('image')

            # Update profile model
            request.user.profile.image = image
            request.user.profile.student_number = student_number
            request.user.profile.student_contact_no = student_contact_no
            request.user.profile.save()

            # Updated the user model 
            request.user.first_name = first_name
            request.user.last_name = last_name
            request.user.username = username
            request.user.email = email
            request.user.save()

        return redirect('profile:edit')

    return render(request, 'user_profile/edit.html', {
        'title': 'Edit Profile',
        'is_staff': is_staff,
    })

def change_password(request):
    is_staff = True if request.user.groups.filter(name='staff') else False

    if request.method == 'POST':
        new_password = request.POST['new_password'] 
        confirm_new_password = request.POST['confirm_new_password'] 

        if new_password == confirm_new_password:
            request.user.set_password(new_password)
            request.user.save()
            messages.info(request, 'Successful')
            return redirect('core:signin')
        else:
            messages.info(request, 'Password don\'t match')
            return redirect('profile:change_password')
            
    return render(request, 'user_profile/change_password.html', {
        'title': 'Change Password',
        'is_staff': is_staff,
    })