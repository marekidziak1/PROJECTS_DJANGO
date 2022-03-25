from django import forms
from . models import Article
class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=['title', 'content']
    def clean(self):
        title=self.cleaned_data.get("title")
        qs = Article.objects.all().filter(title__icontains=title)
        if qs.exists():
            self.add_error('title', f"{title} already exists!!!")
        return self.cleaned_data

class ArticleForm_Old(forms.Form):
    title=forms.CharField()
    content=forms.CharField()
    def clean_title(self):
        title = self.cleaned_data.get('title')
        print(title)
        return title