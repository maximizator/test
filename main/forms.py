from django import forms
from .models import FlightModel

class CreateFlight(forms.ModelForm):
    class Meta:
        model = FlightModel
        
        fields = ['fly_city', 'price_ticket', 'date', 'description']
        
        labels = {
            'fly_city': 'Рейс', 
            'price_ticket': 'Цена билета', 
            'date': 'Дата вылета', 
            'description': 'Класс обслуживания'
        }