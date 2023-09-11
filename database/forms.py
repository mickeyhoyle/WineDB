from django import forms
from datetime import datetime
from django.forms import ModelForm

from .models import Wine, Bottle

class DateInput(forms.widgets.DateInput):
    input_type = 'date'

class WineForm(forms.ModelForm):

    class Meta:
        model = Wine
        fields = ('producer', 'name', 'year', 'alcohol', 'grape', 'colour', 'wine_type', 'notes', 'wishlist', 'date')

        widgets= {
            'date': forms.DateInput(
                attrs={'type':'date'}), 
        }

class BottleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)

    class Meta:
        model = Bottle
        fields = ('wine', 'date_bought', 'bottleprice', 'available', 'drank_on') 

        widgets= {
            'date_bought': forms.DateInput(
                attrs={'type':'date'}), 
        }

# class BottleForm(forms.Form):
#     date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
