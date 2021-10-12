from django.shortcuts import render
from app.forms import CreatePokemonForm

def root(request):
    if request.GET:
        form = CreatePokemonForm(request.GET)
        if form.is_valid():
            creator = form['creator']
            name = form['name']
            height = form['height']
            weight = form['weight']
            region = form['region']
            description = form['description']
            pokemon = [creator, name, type, height, weight, region, description]
            return render(request, "root.html", {"form": form,"pokemon":pokemon})
    else:
        form = CreatePokemonForm()
    return render(request, "root.html", {"form":form})
