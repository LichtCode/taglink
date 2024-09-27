from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, Q
from user.models import User, SocialTag
from django.http import HttpResponseForbidden, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Portfolio, Project, Interaction, ResourceLink, ProjectImage
from .forms import PortfolioForm, ProjectForm, ResourceLinkFormSet, ProjectImageFormSet

@login_required
def portfolio_create(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)

        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user
            portfolio.save()

            return redirect('user-profile')
    else:
        form = PortfolioForm()

    context = {
        'form': form,
    }
    return render(request, 'portfolio/portfolio-form.html', context)


@login_required
def project_create(request):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        resource_link_formset = ResourceLinkFormSet(request.POST, prefix='links')
        project_image_formset = ProjectImageFormSet(request.POST, request.FILES, prefix='images')

        if project_form.is_valid() and resource_link_formset.is_valid() and project_image_formset.is_valid():
            project = project_form.save(commit=False)
            project.portfolio = request.user.portfolio  # Assuming a user has a portfolio
            project.save()

            resource_link_formset.instance = project
            resource_link_formset.save()

            project_image_formset.instance = project
            project_image_formset.save()

            return redirect('portfolio-detail', pk=project.portfolio.pk)
    else:
        project_form = ProjectForm()
        resource_link_formset = ResourceLinkFormSet(prefix='links')
        project_image_formset = ProjectImageFormSet(prefix='images')

    context = {
        'project_form': project_form,
        'resource_link_formset': resource_link_formset,
        'project_image_formset': project_image_formset,
    }
    return render(request, 'portfolio/create_project.html', context)


@login_required
def portfolio_detail(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    user = portfolio.user
    social_tags = SocialTag.objects.filter(user=user).first()
    projects = Project.objects.filter(portfolio=portfolio)
    likes_count = portfolio.interactions.filter(liked=True).count()
    comments = portfolio.interactions.exclude(comment__isnull=True)

    if request.method == 'POST':
        if 'delete' in request.POST:
            if request.user == portfolio.user:
                portfolio.delete()
                return redirect('user-profile')  # Redirect to the list of portfolios after deletion
            else:
                return HttpResponseForbidden("You are not allowed to delete this portfolio.")  # Unauthorized attempt

        if 'like' in request.POST:
            interaction, created = Interaction.objects.get_or_create(user=request.user, portfolio=portfolio)
            interaction.liked = not interaction.liked
            interaction.save()

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'likes_count': portfolio.interactions.filter(liked=True).count()})
            
            return HttpResponseRedirect(reverse('portfolio_detail', args=[pk]))

        elif 'comment' in request.POST:
            comment_text = request.POST.get('comment')
            if comment_text:
                Interaction.objects.create(user=request.user, portfolio=portfolio, comment=comment_text)
            
            return HttpResponseRedirect(reverse('portfolio_detail', args=[pk]))

    context = {
        'portfolio': portfolio,
        'user': user,
        'social_tags': social_tags,
        'projects': projects,
        'likes_count': likes_count,
        'comments': comments,
    }
    return render(request, 'portfolio/portfolio-detail.html', context)
    


@login_required
def portfolio_update(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk, user=request.user)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('portfolio_detail', pk=portfolio.pk)
    else:
        form = PortfolioForm(instance=portfolio)
    return render(request, 'portfolio/portfolio_form.html', {'form': form})

@login_required
def portfolio_delete(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk, user=request.user)
    if request.method == 'POST':
        portfolio.delete()
        return redirect('user-profile')
    return render(request, 'portfolio/portfolio_detail.html', {'portfolio': portfolio})
