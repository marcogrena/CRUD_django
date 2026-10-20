"""
LIVELLO FORM: collega il modello ai campi HTML.

ModelForm genera da solo i campi <input>, la validazione dei dati
(tipi, lunghezze massime, campi obbligatori) e il salvataggio nel db.
"""
from django import forms

from .models import Prodotto


class ProdottoForm(forms.ModelForm):
    class Meta:
        model = Prodotto
        fields = ["nome", "prezzo", "colore", "capacita"]  # id escluso: lo assegna il db
