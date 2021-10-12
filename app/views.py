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


def main(request):
    return render(request, "dex.html")


def pokemon(request):
    return render(request, "pokemon.html")
