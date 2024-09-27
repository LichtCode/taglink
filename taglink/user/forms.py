from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, SocialTag

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=150, required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'profile_picture', 'bio']

class SocialTagForm(forms.ModelForm):
    class Meta:
        model = SocialTag
        fields = ['linkedin', 'github', 'twitter']
        widgets = {
            'linkedin': forms.URLInput(attrs={'placeholder': 'LinkedIn URL', 'class': 'form-control'}),
            'github': forms.URLInput(attrs={'placeholder': 'GitHub URL', 'class': 'form-control'}),
            'twitter': forms.URLInput(attrs={'placeholder': 'Twitter URL', 'class': 'form-control'}),
        }
        labels = {
            'linkedin': 'LinkedIn',
            'github': 'GitHub',
            'twitter': 'Twitter',
        }