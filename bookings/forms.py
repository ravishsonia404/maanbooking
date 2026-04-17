from django import forms
from .models import Ride

class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['name', 'email', 'pickup', 'drop', 'date', 'time']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter your email'
            }),
            'pickup': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Pickup location'
            }),
            'drop': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Drop location'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control form-control-lg',
                'type': 'date'
            }),
            'time': forms.TimeInput(attrs={
                'class': 'form-control form-control-lg',
                'type': 'time'
            }),
        }
