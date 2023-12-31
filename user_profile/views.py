from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

@login_required
def index(request):
    return render(request, 'user_profile/index.html', {
        'title': 'Profile',
        'is_staff': request.is_staff,
    })

@login_required
def edit(request):
    if request.method == 'POST':
        user = request.user
        profile = user.profile

        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.username = request.POST.get('username', '')
        user.email = request.POST.get('email', '')

        # Validating and handling student_number and student_contact_no inputs
        student_number = request.POST.get('student_number', '')
        student_contact_no = request.POST.get('student_contact_no', '')

        if student_number:
            profile.student_number = student_number

        if student_contact_no:
            profile.student_contact_no = student_contact_no

        # Handling image upload
        if request.FILES.get('image'):
            profile.image = request.FILES['image']

        profile.save()
        user.save()

        return redirect('profile:edit')

    return render(request, 'user_profile/edit.html', {
        'title': 'Edit Profile',
        'is_staff': request.is_staff,
    })

@login_required
def change_password(request):
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
        'is_staff': request.is_staff,
    })