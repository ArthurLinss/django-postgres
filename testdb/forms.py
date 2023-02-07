from django import forms 
from django.forms.models import (
    inlineformset_factory,
    modelform_factory,
    modelformset_factory
)
from .models import Teacher, Subject, Book 


class BookForm(forms.ModelForm):

    class Meta:
        model = Book 
        fields = (
            "title",
            "number_of_pages",
        )

BookFormSet = inlineformset_factory(
    Teacher, 
    Book,
    BookForm,
    can_delete=True, 
    min_num = 0, 
    extra = 1, 
)