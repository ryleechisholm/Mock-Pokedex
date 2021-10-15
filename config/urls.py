from django.urls import path
import app.views

urlpatterns = [
    path('create/', app.views.create, name="create"),
    path('', app.views.dex, name="dex"),
    path('entry/<pokemon>/', app.views.entry, name="entry"),
    path('user-entry/<pokemon>/', app.views.user_entry, name="user-entry")
]
     
