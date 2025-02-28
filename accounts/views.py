from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
import re
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Profile

def home(request):
    now = timezone.localtime(timezone.now())
    return render(request, 'home.html', {'now': now})

def login_view(request):

    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        if(not User.objects.filter(username=username).exists()):
            messages.error(request, "User does not exist.")
            return redirect('login')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile', username=user.username)
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('/accounts/login')

def profile(request, username):
    user_profile = get_object_or_404(User, username__iexact=username)
    profile_data, _ = Profile.objects.get_or_create(user=user_profile)
    return(render(request, 'accounts/profile.html', {'user_profile': user_profile, 'profile': profile_data}))

@login_required
def edit_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if(request.method == 'POST'):
        new_username = request.POST.get('username', '').strip()
        new_email = request.POST.get('email', '').strip()
        new_password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()
        new_bio = request.POST.get('bio', '').strip()
        new_profile_picture = request.FILES.get('profile_picture')

        if(new_username and new_username != user.username):
            
            if(User.objects.exclude(id=user.id).filter(username=new_username).exists()):
                messages.error(request, "Username already taken!")
                return redirect('edit_profile')
            
            user.username = new_username

        if(new_email and new_email != user.email):
            user.email = new_email

        if(new_password):

            if(new_password != confirm_password):
                messages.error(request, "Passwords do not match!")
                return redirect('edit_profile')
            
            user.set_password(new_password)
            update_session_auth_hash(request, user)
        
        if(new_bio == ""):
            new_bio = profile.bio

        profile.bio = new_bio

        if(new_profile_picture):
            print("New uploaded", new_profile_picture.name)
            profile.profile_picture = new_profile_picture
        else:
            print("nothing uploaded")

        user.save()
        profile.save()

        messages.success(request, "Profile updated successfully!")
        return redirect('profile', username=user.username)
    
    return render(request, 'accounts/edit_profile.html')