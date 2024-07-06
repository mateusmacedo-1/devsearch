from django.forms import ModelForm
from django import forms
from .models import Project

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