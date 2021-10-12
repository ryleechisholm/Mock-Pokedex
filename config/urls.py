from django.urls import path
import app
urlpatterns = [
    path('', app.views.root, name="root"),
]
