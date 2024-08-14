from django.forms import HiddenInput, ModelForm
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
        fields = ('recipient', 'sender', 'name', 'email', 'subject', 'body')
    
    def __init__(self, *args, **kwargs):
        self.sender = kwargs.pop('sender', None)
        self.recipient = kwargs.pop('recipient', None)
        self.name = self.sender.name if self.sender else None
        self.email = self.sender.email if self.sender else None
        super(MessageForm, self).__init__(*args, **kwargs)
        
        self.fields['recipient'] = forms.ModelChoiceField(queryset=self.fields['recipient'].queryset.exclude(id=self.sender.id) if self.sender else self.fields['recipient'].queryset)
        self.fields['recipient'].initial = self.recipient
        
        if self.sender:
            self.fields['sender'].widget = HiddenInput()
            self.fields['name'].widget = HiddenInput()
            self.fields['email'].widget = HiddenInput()
            self.fields['sender'].initial = self.sender
            self.fields['name' ].initial = self.sender.name
            self.fields['email'].initial = self.sender.email

        for k, v in self.fields.items():
            v.widget.attrs.update({'class':'input'})

    def clean(self):
        cleaned_data = super(MessageForm, self).clean()

        if cleaned_data['sender'].id == cleaned_data['recipient'].id:
            raise forms.ValidationError('Você não pode enviar uma mensagem para você mesmo.')
        return cleaned_data
