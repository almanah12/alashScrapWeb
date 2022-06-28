from django import forms

from .models import Personal


class PersonalForm(forms.Form):
    login = forms.EmailField(max_length=50, initial=Personal.objects.get(id=1).login,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}),
                             label='Логин')
    password = forms.CharField(max_length=50, initial=Personal.objects.get(id=1).password,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               label='Пароль')
    name_shop = forms.CharField(max_length=30, initial=Personal.objects.get(id=1).name_shop,
                                widget=forms.TextInput(attrs={'class': 'form-control'}),
                                label='Имя магазина')
    id_partner = forms.IntegerField(initial=Personal.objects.get(id=1).id_partner,
                                    widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                    label='ID партнера')
    city = forms.CharField(max_length=50, initial=Personal.objects.get(id=1).city,
                           widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='Город')
