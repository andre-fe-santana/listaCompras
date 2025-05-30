from django.urls import path, include
from lista import views

app_name = "lista"

urlpatterns = [
    path('', views.mostrarLista, name="mostrarLista"),
]