from django import forms
from main.models import Zombie, Twit


class ZombieForm(forms.ModelForm):
    class Meta:
        model = Zombie


class TwitForm(forms.ModelForm):
    class Meta:
        model = Twit
