from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.portfolio_create, name='create_portfolio'),
    path('<int:pk>/', views.portfolio_detail, name='portfolio_detail'),
    path('<int:pk>/edit/', views.portfolio_update, name='portfolio_update'),
    path('<int:pk>/delete/', views.portfolio_delete, name='portfolio_delete'),
    path('<int:pk>/like/', views.portfolio_detail, name='like_portfolio'),
    path('<int:pk>/comment/', views.portfolio_detail, name='add_comment'),
]

