from django.forms import ModelForm
from django import forms
from .models import Project, Review

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'featured_image', 'source_link', 'demo_link', 'tags')
        widgets = {
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'})
        }
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        for k, v in self.fields.items():
            v.widget.attrs.update({'class':'input', 'placeholder': f'Add {k}'})

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('value', 'body', )
        labels = {
            'body': 'Add a comment',
            'value': 'Place your vote'
        }

    def __init__(self, *args, **kwargs):
        self.owner = kwargs.pop('owner', None)
        self.project = kwargs.pop('project', None)
        super(ReviewForm, self).__init__(*args, **kwargs)
        for v in self.fields.values():
            v.widget.attrs.update({'class':'input'})
        
    def clean(self):
        cleaned_data = super(ReviewForm, self).clean()
        if Review.objects.filter(owner=self.owner, project=self.project).exists():
            raise forms.ValidationError('You have already reviewed this project.')
        return cleaned_data