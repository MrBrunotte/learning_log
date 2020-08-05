from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """Inherits from ModelForm in Django"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    """Inherits from forms.ModelForm in Django"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
