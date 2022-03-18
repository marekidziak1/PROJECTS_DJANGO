from django import forms
from .models import Item, ToDoList
class CreateNewList(forms.Form):
    name=forms.CharField(label="name",max_length = 200)
    #check = forms.BooleanField(required=False)
class CreateNewItem(forms.ModelForm):
    #todolist = forms.ModelChoiceField()                 #
    todolist = forms.CharField(widget=forms.TextInput(attrs={"placeholder":""}))
    text = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"input your text here"}))
    complete = forms.BooleanField(required=False)
    class Meta:
        model = Item
        fields = ['todolist', 'text','complete']

