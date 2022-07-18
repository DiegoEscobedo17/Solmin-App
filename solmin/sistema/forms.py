from dataclasses import fields
from django import forms
from .models import *

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = '__all__'