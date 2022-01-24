from .models import City, Region
from django.forms import ModelForm, TextInput, NumberInput, Select


class CityUpdateForm(ModelForm):
    """Форма для редактирования водителя"""
    class Meta:
        model = City
        fields = ['name', 'age']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
            'age': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'})
        }