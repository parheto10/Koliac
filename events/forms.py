from django.forms import ModelForm, DateInput, DateTimeInput
from .models import Annonce

class AnnonceForm(ModelForm):
    class Meta:
        model = Annonce
        fields = '__all__'
        exclude = ['user', 'participant', 'fare_part']


class AnnonceUpdateForm(ModelForm):
    class Meta:
        model = Annonce
        fields = '__all__'
        exclude = ['user', 'participant']