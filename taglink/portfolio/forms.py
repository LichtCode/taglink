from django import forms
from django.forms import inlineformset_factory
from .models import Portfolio, Project, ResourceLink, ProjectImage

class PortfolioForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Enter tags separated by commas.")

    class Meta:
        model = Portfolio
        fields = ['title', 'description', 'tags']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']

class ResourceLinkForm(forms.ModelForm):
    class Meta:
        model = ResourceLink
        fields = ['name', 'url']

class ProjectImageForm(forms.ModelForm):
    class Meta:
        model = ProjectImage
        fields = ['image']

ResourceLinkFormSet = inlineformset_factory(
    Project, ResourceLink, form=ResourceLinkForm, extra=1, can_delete=True
)

ProjectImageFormSet = inlineformset_factory(
    Project, ProjectImage, form=ProjectImageForm, extra=1, can_delete=True
)