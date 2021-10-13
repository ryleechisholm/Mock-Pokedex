from django.shortcuts import render
from app.forms import CreatePokemonForm

def create(request):
    if request.GET:
        form = CreatePokemonForm(request.GET)
        if form.is_valid():
            creator = form['creator']
            name = form['name']
            height = form['height']
            weight = form['weight']
            region = form['region']
            description = form['description']
            type = form['type']
            type2 = form['type2']
            pokemon = [creator, name, type, height, weight, region, description, type, type2]
            return render(request, "create.html", {"form": form,"pokemon":pokemon})
    else:
        form = CreatePokemonForm()
    return render(request, "create.html", {"form":form})

def dex(request):
    context = {
        "Pokemon": {
            "bulbasaur": "Bulbasaur",
            "ivysaur": "Ivysaur",
            "venusaur": "Venusaur",
            "charmander": "Charmander"}}
    return render(request, "dex.html", context)

            
class Gen_1:    
    def __init__(self, name, height, weight, region, description, type1, type2):
        self.name = name
        self.height = height
        self.weight = weight
        self.region = region
        self.description = description
        self.types = [type1, type2]

def entry(request, pokemon):
    context = {
        "pokemon": pokemon,
        "Pokemon": {
            "bulbasaur": Gen_1("Bulbasaur", 0.7, 6.9, "Kanto", "Bulbasaur can be seen napping in bright sunlight.  There is a seed on its back.  By soaking up the sun's rays, the seed grows progressively larger.", "Grass", "Poison"),
            "ivysaur": Gen_1("Ivysaur", 0.5, 0.5, "Kanto", "When the bulb on its back grows large, it appears to lose the ability to stand on its hind legs.", "Grass", "Poison"),
            "venusaur": Gen_1("Venusaur", 0.5, 0.5, "Kanto", "Its plant blooms when it is absorbing solar energy.  It stays on the move to seek sunlight.", "Grass", "Poison"),
            "charmander": Gen_1("Charmander", 0.6, 8.5, "Kanto", "The flame that burns at the tip of its tail is an indication of its emotions.  The flame wavers when Charmander is enjoying itself.  If the pokémon becomes enraged the flame burns fiercely.", "Fire", None),}}
    return render(request, "entry.html", context)

