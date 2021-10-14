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
 

TYPES2 = [('--Choose A Type--',
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
    ('ice','Ice')
    ),)]

class CreatePokemonForm(forms.Form):
    creator = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Your Name', 'style': 'width: 300px;'}), min_length=0, max_length=100, required=True, label="What is your Name?")
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Pokémon Name', 'style': 'width: 300px;'}), min_length=0, max_length=100, required=True, label="What would you like to name your Pokémon?")
    height = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Pokémon Height', 'style': 'width: 300px;'}), min_value=1, max_value=60, required=True, label="How tall is your Pokémon? (in meters)")
    weight = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Pokémon Weight', 'style': 'width: 300px;'}), min_value=1, required=True, label="How much does your Pokémon weight? (in kilograms)")
    region = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Pokémon Birth Region', 'style': 'width: 300px;'}), min_length=0, max_length=500, required=True, label="What region is your Pokémon from?")
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Pokémon Description', 'style': 'width: 300px;'}), min_length=0, max_length=1000, required=True, label="Describe your Pokémon.")
    type1 = forms.CharField(label="What type is your Pokémon?", widget=forms.Select(choices=TYPES, attrs={'placeholder': 'Pokémon Description', 'style': 'width: 300px;'}), )
    type2 = forms.CharField(label="What is your other type?", widget=forms.Select(choices=TYPES, attrs={'placeholder': 'Pokémon Description', 'style': 'width: 300px;'}) )

    
    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data['type1'] == cleaned_data['type2']:
            self.add_error('type2', 'Type 2 cannot be the same as Type 1!')
        return cleaned_data


class TypeForm(forms.Form):
    poketype = forms.CharField(label="What type are you searching?", widget=forms.Select(choices=TYPES2, attrs={'placeholder': 'Pokémon Type', 'style': 'width: 300px;'}), )
