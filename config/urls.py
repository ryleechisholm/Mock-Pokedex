from django.urls import path
import app.views
urlpatterns = [
    path('', app.views.root, name="root"),
]
