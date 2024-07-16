from django.forms import ModelForm
from django import forms
from .models import Skill

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ('name', 'description')
        widgets = {
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'})
        }
    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        for k, v in self.fields.items():
            v.widget.attrs.update({'class':'input', 'placeholder': f'Add {k}'})