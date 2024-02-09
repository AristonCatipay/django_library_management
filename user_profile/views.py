from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from address.models import Region, Province, City_Municipality, Barangay

@login_required
def index(request):
    return render(request, 'profile/index.html', {
        'title': 'Profile',
        'is_staff': request.is_staff,
    })

@login_required
def update_profile(request):
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
        messages.success(request, 'Success! The profile has been edited.')
        return redirect('profile:edit')

    return render(request, 'profile/update_profile.html', {
        'title': 'Edit Profile',
        'is_staff': request.is_staff,
    })

@login_required
def update_address(request):
    regions = Region.objects.all()

    if request.method == 'POST':
        try:
            region = request.POST['region']
            province = request.POST['province']
            city_municipality = request.POST['city_municipality']
            barangay = request.POST['barangay']
            location = request.POST['location']

            region = get_object_or_404(Region, pk=region)
            province = get_object_or_404(Province, pk=province)
            city_municipality = get_object_or_404(City_Municipality, pk=city_municipality)
            barangay = get_object_or_404(Barangay, pk=barangay)
            request.user.profile.region = region
            request.user.profile.province = province
            request.user.profile.city_municipality = city_municipality
            request.user.profile.barangay = barangay
            request.user.profile.location = location
            request.user.profile.save()

            messages.success(request, "User address updated successfully! Your changes have been saved.")
            return redirect('profile:update_address')
        except Exception as e:
            messages.error(request, f"Failed to update address. {e}")
    
    return render(request, 'profile/update_address.html', {
        'title': 'Edit User Address',
        'regions': regions,
    })

@login_required
def load_province(request):
    region = request.GET.get('region')
    provinces = Province.objects.filter(region=region)
    return render(request, 'profile/load/province_options.html', {
        'provinces': provinces,
    })

@login_required
def load_city_municipality(request):
    province = request.GET.get('province')
    city_municipalities = City_Municipality.objects.filter(province=province)
    return render(request, 'profile/load/city_municipality_options.html', {
        'city_municipalities': city_municipalities,
    })

@login_required
def load_barangay(request):
    city_municipality = request.GET.get('city_municipality')
    barangays = Barangay.objects.filter(city_municipality=city_municipality)
    return render(request, 'profile/load/barangay_options.html', {
        'barangays': barangays,
    })

@login_required
def update_password(request):
    if request.method == 'POST':
        old_password = request.POST['old_password'] 
        new_password = request.POST['new_password'] 
        confirm_new_password = request.POST['confirm_new_password'] 

        if request.user.check_password(old_password):
            if new_password == confirm_new_password:
                request.user.set_password(new_password)
                request.user.save()
                messages.success(request, 'Success! The password has been edited.')
                return redirect('core:signin')
            else:
                messages.error(request, 'Failed to update password. Password don\'t match')
                return redirect('profile:change_password')
        else:
            messages.error(request, 'Failed to update password. Old password does not match.')
            return redirect('profile:change_password')
            
    return render(request, 'profile/update_password.html', {
        'title': 'Change Password',
        'is_staff': request.is_staff,
    })