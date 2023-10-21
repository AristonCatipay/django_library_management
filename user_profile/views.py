from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages

from . models import Profile

User = get_user_model()

def index(request):
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    return render(request, 'user_profile/index.html', {
        'title': 'Profile',
        'profile': profile,
    })

def edit(request):
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

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

            image = profile.image

            # Update profile model
            profile.image = image
            profile.student_number = student_number
            profile.student_contact_no = student_contact_no
            profile.save()

            # Updated the user model 
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()

        if request.FILES.get('image') != None:
            image = request.FILES.get('image')

            # Update profile model
            profile.image = image
            profile.student_number = student_number
            profile.student_contact_no = student_contact_no
            profile.save()

            # Updated the user model 
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()

        return redirect('profile:edit')

    return render(request, 'user_profile/edit.html', {
        'title': 'Edit Profile',
        'profile': profile,
    })

def change_password(request):
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        new_password = request.POST['new_password'] 
        confirm_new_password = request.POST['confirm_new_password'] 

        if new_password == confirm_new_password:
            user.set_password(new_password)
            user.save()
            messages.info(request, 'Successful')
            return redirect('core:signin')
        else:
            messages.info(request, 'Password don\'t match')
            return redirect('profile:change_password')
            
    return render(request, 'user_profile/change_password.html', {
        'title': 'Change Password',
        'profile': profile,
    })