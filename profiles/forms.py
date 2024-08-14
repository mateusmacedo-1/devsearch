from django.forms import ModelForm
from django import forms
from .models import Skill, Message

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

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('recipient', 'name', 'email', 'subject', 'body')
    
    def __init__(self, *args, **kwargs):
        self.sender = kwargs.pop('sender', None)
        self.recipient = kwargs.pop('recipient', None)
        super(MessageForm, self).__init__(*args, **kwargs)

        self.fields['recipient'].initial = self.recipient
        if self.sender:
            self.fields['name'].initial = self.sender.name
            self.fields['email'].initial = self.sender.email
        for k, v in self.fields.items():
            v.widget.attrs.update({'class':'input'})
