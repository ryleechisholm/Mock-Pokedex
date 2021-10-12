from django import forms
from django.db.models.deletion import SET_DEFAULT
from django.forms.fields import GenericIPAddressField
from app.models import Settings

class CreatePokemonForm(forms.Form):
    creator = forms.CharField(min_length=0,max_length=50, required=True)
    name = forms.CharField(min_length=0,max_length=30, required=True)
    grass = forms.BooleanField(required=False)
    fire = forms.BooleanField(required=False)
    water = forms.BooleanField(required=False)
    flying = forms.BooleanField(required=False)
    dragon = forms.BooleanField(required=False)
    steel = forms.BooleanField(required=False)
    ghost = forms.BooleanField(required=False)
    dark = forms.BooleanField(required=False)
    psychic = forms.BooleanField(required=False)
    fighting = forms.BooleanField(required=False)
    normal = forms.BooleanField(required=False)
    bug = forms.BooleanField(required=False)
    poison = forms.BooleanField(required=False)
    rock = forms.BooleanField(required=False)
    ground = forms.BooleanField(required=False)
    electric = forms.BooleanField(required=False)
    fairy = forms.BooleanField(required=False)
    ice = forms.BooleanField(required=False)
    height = forms.IntegerField(min_value=0, required=True)
    weight = forms.IntegerField(min_value=0, required=True)
    region = forms.CharField(min_length=0,max_length=30, required=True)
    description = forms.CharField(min_length=0,max_length=200, required=True)

    class Meta:
        model = Settings



