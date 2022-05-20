from django import forms
from .models import UsedCar

class UsedCarsForm(forms.ModelForm):
    class Meta:
        model=UsedCar
        fields='__all__'
        widgets = {
            
            'ad-title': forms.TextInput(attrs={'class':'form-control'}),
            'Describtion': forms.TextInput(attrs={'class':'form-control'}),
            'travelled_KM': forms.NumberInput(attrs={'class':'form-control'}),
            'owner_name': forms.TextInput(attrs={'class':'form-control'}),
            'owner_phonenumber': forms.NumberInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'type': forms.Select(attrs={'class':'form-control'}),
            'brand': forms.Select(attrs={'class':'form-control'}),
            'transmission_type': forms.Select(attrs={'class':'form-control'}),
            'CC': forms.NumberInput(attrs={'class':'form-control'}),
            'model_year': forms.Select(attrs={'class':'form-control'}),
            'used_since': forms.Select(attrs={'class':'form-control'}),
            'fuel': forms.Select(attrs={'class':'form-control'}),
            'color': forms.TextInput(attrs={'class':'form-control'}),
            'extra_equipment': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),   
        }