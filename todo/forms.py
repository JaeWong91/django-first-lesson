from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:     # The inner 'Meta' class just gives our form some information about itself.
        model = Item
        fields = ['name', 'done']
