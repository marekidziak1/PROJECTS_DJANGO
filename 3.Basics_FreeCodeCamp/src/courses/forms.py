from .models import Course
from django import forms

class CourseModelForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"input yor title"}))
    class Meta:
        model = Course
        fields=['title']
    