from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('user-profile', views.user_profile, name='user-profile'),
    path('user-profile-update/', views.user_profile_update, name='user-profile-update'),
]