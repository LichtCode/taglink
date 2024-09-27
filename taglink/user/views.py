from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegistrationForm, UserUpdateForm, SocialTagForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .models import SocialTag
from portfolio.models import Portfolio

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home-page')
    else:
        form = UserRegistrationForm()
        
    context = { 
        'form': form,
    }
    return render(request, 'user/register-or-login.html', context)

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home-page')
    else:
        form = AuthenticationForm()
    return render(request, 'user/register-or-login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def user_profile_update(request):
    user = request.user
    social_tags, created = SocialTag.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, request.FILES, instance=user)
        social_tag_form = SocialTagForm(request.POST, instance=social_tags)

        if user_form.is_valid() and social_tag_form.is_valid():
            user_form.save()
            social_tag_form.save()

            # Update the password if provided
            new_password = user_form.cleaned_data.get('password')
            if new_password:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)

            return redirect('user-profile')

    else:
        user_form = UserUpdateForm(instance=user)
        social_tag_form = SocialTagForm(instance=social_tags)

    context = {
        'form': user_form,
        'social_tag_form': social_tag_form,
    }
    return render(request, 'user/user-detail-edit.html', context)

@login_required
def user_profile(request):
    user = request.user
    social_tags = SocialTag.objects.filter(user=user).first()
    portfolios = Portfolio.objects.filter(user=user)

    context = {
        'user': user,
        'social_tags': social_tags,
        'portfolios': portfolios,
    }
    return render(request, 'user/user-detail.html', context)