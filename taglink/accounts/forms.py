from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from .models import Portfolio, Project

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('bio', 'profile_picture', 'social_links')



class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'description']  # Portfolio fields

class ProjectForm(forms.ModelForm):
    portfolios = forms.ModelMultipleChoiceField(queryset=Portfolio.objects.all(), 
                                                widget=forms.CheckboxSelectMultiple, 
                                                required=True)

    class Meta:
        model = Project
        fields = ['title', 'description', 'project_link', 'project_images', 'portfolios']  # Include portfolios in the form