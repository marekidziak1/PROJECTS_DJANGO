from .models import Product
from django import forms
class ProductRawForm(forms.Form):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={
                                        "placeholder":"your title"
                                    }))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
                                        "class":"new-class-name two",
                                        "id":"my_id",
                                        "rows":20,
                                        "cols":120
                                    }))
    price       = forms.DecimalField(initial=199.99)
    summary     = forms.CharField()
    featured    = forms.BooleanField()
    def clean_my_title(self, *args, **kwargs):
        title=self.cleaned_data.get("title")
        if 'tytul' in title:
            return title
        else:
            raise forms.ValidationError('tytul is not in title')

class ProductCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"your title"}))
    description = forms.CharField(widget=forms.Textarea)
    class Meta:
        model=Product
        fields =[
            'title',
            'description',
            'price',
            'summary',
            'featured',
        ]