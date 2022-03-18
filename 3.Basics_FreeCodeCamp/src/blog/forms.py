from .models import Article
from django import forms

class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'input your title'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'input your content'}))
    active = forms.CheckboxInput
    class Meta:
        model = Article
        fields=['title', 'content', 'active']