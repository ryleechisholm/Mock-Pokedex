from django.urls import path
import app.views
urlpatterns = [
    path('create', app.views.create, name="create"),
    path('', app.views.main, name="main"),
    path('pokémon/', app.views.pokemon, name="pokemon")
]
