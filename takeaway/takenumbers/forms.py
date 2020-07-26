from django.forms import ModelForm
from .models import Bestellnummer

class BestellnummerForm(ModelForm):
    class Meta:
        model = Bestellnummer
        fields = ['bnum']