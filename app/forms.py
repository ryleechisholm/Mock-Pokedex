from django import forms

TYPES = [('grass','Grass'),
    ('fire','Fire'), 
    ('water','Water'), 
    ('flying','Flying'),
    ('dragon','Dragon'), 
    ('steel','Steel'), 
    ('ghost','Ghost'), 
    ('dark','Dark'),
    ('psychic','Psychic'),
    ('fighting','Fighting'),
    ('normal','Normal'),
    ('bug','Bug'),
    ('poison','Poison'), 
    ('rock','Rock'),
    ('ground','Ground'), 
    ('electric','Electric'), 
    ('fairy','Fairy'), 
    ('ice','Ice'), ]

class CreatePokemonForm(forms.Form):
    Creator = forms.CharField(min_length=0, max_length=100, required=True)
    name = forms.CharField(min_length=0, max_length=100, required=True)
    height = forms.IntegerField(min_value=1, max_value=60, required=True)
    weight = forms.IntegerField(min_value=1, required=True)
    region = forms.CharField(min_length=0, max_length=500, required=True)
    description = forms.CharField(min_length=0, max_length=1000, required=True)
    type = forms.CharField(widget=forms.Select(choices=TYPES))
    type2 = forms.CharField(widget=forms.Select(choices=TYPES))


    

