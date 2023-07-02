from django import forms
from django.forms import ModelForm
from .models import Author, Category
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["name", "description", "author", "category", "is_enable", "file"]


# its same like top
#
#class BookForm(forms.Form):
#    name = forms.CharField(max_length=50)
#    description = forms.CharField(widget=forms.Textarea)
#    author = forms.ModelMultipleChoiceField(queryset=Author.objects.all(),)
#    category = forms.ModelMultipleChoiceField(
#                                            queryset=Category.objects.all(),
#                                            widget=forms.CheckboxSelectMultiple)
#    is_enable = forms.BooleanField()
#    file = forms.FileField()


