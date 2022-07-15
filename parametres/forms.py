# from django.contrib.auth.models import User
import phonenumbers
from django.forms import forms, ModelForm
from django.contrib.auth.forms import UserCreationForm
from phonenumbers import NumberParseException
from django import forms
from .models import User

class BootstrapSelect(forms.Select):
    def __init__(self, size=12, *args, **kwargs):
        self.size = size
        super(BootstrapSelect, self).__init__(attrs={
            'class': 'form-control input-sm',
        })

    def bootwrap_input(self, input_tag):
        classes = 'col-xs-{n} col-sm-{n} col-md-{n}'.format(n=self.size)

        return '''<div class="{classes}">
                    <div class="form-group">{input_tag}</div>
                  </div>
               '''.format(classes=classes, input_tag=input_tag)

    def render(self, *args, **kwargs):
        input_tag = super(BootstrapSelect, self).render(*args, **kwargs)
        return self.bootwrap_input(input_tag)

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        via = forms.ChoiceField(
            choices=[('sms', 'SMS'), ('call', 'APPEL')],
            widget=BootstrapSelect(size=3))
        fields = [
            'nom',
            'username',
            'email',
            'password1',
            'password2',
            'contact1',
        ]
    # def clean(self):
    #     data = self.cleaned_data
    #     phone_number = data['phone_number']
    #     try:
    #         phone_number = phonenumbers.parse(phone_number, None)
    #         if not phonenumbers.is_valid_number(phone_number):
    #             self.add_error('phone_number', 'Le Numéro Saisi est Incorrect')
    #     except NumberParseException as e:
    #         self.add_error('phone_number', e)

    # def clean_username(self):
    #     username = self.cleaned_data.get("username")
    #     qs = User.objects.filter(username__iexact=username)
    #     if not qs.exists:
    #         raise forms.ValidationError("Un Utilisateur Avec ce nom Existe déjà, Réssayer SVP !!!")
    #     return username
    #
    # def clean_username(self):
    #     username = self.cleaned_data.get("username")
    #     qs = User.objects.filter(username__iexact=username)
    #     if not qs.exists:
    #         raise forms.ValidationError("Un Utilisateur Avec ce nom Existe déjà, Réssayer SVP !!!")
    #     return username

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['nom', 'contact1', 'contact2', 'orange_money', 'mtn_money', 'moov_money', 'adresse', 'image', 'type_piece', 'num_piece', 'piece']



class BootstrapInput(forms.TextInput):
    def __init__(self, placeholder, size=12, *args, **kwargs):
        self.size = size
        super(BootstrapInput, self).__init__(attrs={
            'class': 'form-control input-sm',
            'placeholder': placeholder
        })

    def bootwrap_input(self, input_tag):
        classes = 'col-xs-{n} col-sm-{n} col-md-{n}'.format(n=self.size)

        return '''<div class="{classes}">
                    <div class="form-group">{input_tag}</div>
                  </div>
               '''.format(classes=classes, input_tag=input_tag)

    def render(self, *args, **kwargs):
        input_tag = super(BootstrapInput, self).render(*args, **kwargs)
        return self.bootwrap_input(input_tag)

class VerificationForm(forms.Form):
    phone_number = forms.CharField(
        widget=forms.HiddenInput())
    via = forms.ChoiceField(
        choices=[('sms', 'SMS'), ('call', 'APPEL')],
        widget=BootstrapSelect(size=3))

    def clean(self):
        data = self.cleaned_data
        phone_number = data['phone_number']
        try:
            phone_number = phonenumbers.parse(phone_number, None)
            if not phonenumbers.is_valid_number(phone_number):
                self.add_error('phone_number', 'Le Numéro Saisi est Incorrect')
        except NumberParseException as e:
            self.add_error('phone_number', e)

class TokenForm(forms.Form):
    token = forms.CharField(
        widget=BootstrapInput('Verification Token', size=6))