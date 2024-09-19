from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('create-portfolio/', views.create_portfolio, name='create_portfolio'),
    path('update-portfolio/<int:portfolio_id>/', views.update_portfolio, name='update_portfolio'),
    path('delete-portfolio/<int:portfolio_id>/', views.delete_portfolio, name='delete_portfolio'),
    path('create-project/', views.create_project, name='create_project'),
]