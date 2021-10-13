from django.urls import path
import app.views
urlpatterns = [
    path('create', app.views.create, name="create"),
    path('', app.views.main, name="main"),
    path('', views.dex, name="dex"),
    path('entry/<pokemon>', views.entry, name="entry")
]
