"""
LIVELLO ROTTE dell'app. Questo file è incluso in hello_world/urls.py con prefisso "prodotti/".

Rotta completa            -> vista            -> operazione
GET  /prodotti/           -> views.lista      -> Read (elenco)
GET/POST /prodotti/nuovo/ -> views.crea       -> Create
GET/POST /prodotti/<id>/modifica/ -> views.modifica -> Update
GET/POST /prodotti/<id>/elimina/  -> views.elimina  -> Delete

<int:pk> cattura l'id dall'URL e lo passa alla vista come argomento `pk`.
`name` permette di richiamare la rotta con {% url 'prodotti:lista' %} o redirect().
"""
from django.urls import path

from . import views

app_name = "prodotti"  # namespace: "prodotti:lista", "prodotti:crea", ...

urlpatterns = [
    path("", views.lista, name="lista"),
    path("nuovo/", views.crea, name="crea"),
    path("<int:pk>/modifica/", views.modifica, name="modifica"),
    path("<int:pk>/elimina/", views.elimina, name="elimina"),
]
