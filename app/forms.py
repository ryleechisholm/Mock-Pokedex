from django import forms

TYPES = [('--Choose One--',
    (
    ('grass','Grass'),
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
    ('ice','Ice'),
    ('none', "None"),
    ),)]
 

class CreatePokemonForm(forms.Form):
    Creator = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Your Name', 'style': 'width: 300px;'}), min_length=0, max_length=100, required=True, label="What is your Name?")
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Pokémon Name', 'style': 'width: 300px;'}), min_length=0, max_length=100, required=True, label="What would you like to name your Pokémon?")
    height = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Pokémon Height', 'style': 'width: 300px;'}), min_value=1, max_value=60, required=True, label="How tall is your Pokémon?")
    weight = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Pokémon Weight', 'style': 'width: 300px;'}), min_value=1, required=True, label="How much does you Pokémon weight?")
    region = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Pokémon Birth Region', 'style': 'width: 300px;'}), min_length=0, max_length=500, required=True, label="What region is your Pokémon from?")
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Pokémon Description', 'style': 'width: 300px;'}), min_length=0, max_length=1000, required=True, label="Describe your Pokémon.")
    type = forms.CharField(widget=forms.Select(choices=TYPES), label="What type is your Pokémon?")
    type2 = forms.CharField(widget=forms.Select(choices=TYPES), label="What is your other type?")

