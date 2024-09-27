from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.db.models import Sum, Count, Q
from portfolio.models import Portfolio
from user.models import User
from user.forms import UserRegistrationForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to the index page after successful registration
    else:
        form = UserRegistrationForm()

    context = {
        'user': request.user if request.user.is_authenticated else None,
        'form': form,
    }
    return render(request, 'index.html', context)

def home(request):
    top_portfolios = Portfolio.objects.annotate(
        num_likes=Count('interactions', filter=Q(interactions__liked=True)),
        num_comments=Count('interactions', filter=Q(interactions__comment__isnull=False))
    ).order_by('-num_likes', '-num_comments')[:4]
    
    users_with_likes = []
    for user in User.objects.all():
        total_likes = Portfolio.objects.filter(user=user).aggregate(
            total_likes=Sum('interactions__liked', filter=Q(interactions__liked=True))
        )['total_likes'] or 0
        users_with_likes.append((user, total_likes))

    top_talents = sorted(users_with_likes, key=lambda x: x[1], reverse=True)[:4]

    context = {
        'top_portfolios': top_portfolios,
        'top_talents': [user[0] for user in top_talents],
        'new_talents': User.objects.order_by('-date_joined')[:4], 
    }
    return render(request, 'home.html', context)