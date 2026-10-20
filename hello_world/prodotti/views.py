"""
LIVELLO LOGICA (viste): riceve la richiesta HTTP, usa il modello per leggere/scrivere
sul db e sceglie il template HTML da mostrare. Qui non c'è né SQL né HTML:
- SQL  -> gestito dall'ORM di Django tramite models.py
- HTML -> nei template in templates/prodotti/
"""
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProdottoForm
from .models import Prodotto


def lista(request):
    # READ (elenco): SELECT * FROM prodotti_prodotto ORDER BY id
    prodotti = Prodotto.objects.all().order_by("id")
    return render(request, "prodotti/lista.html", {"prodotti": prodotti})


def crea(request):
    # CREATE: GET mostra il form vuoto, POST lo valida e fa INSERT
    if request.method == "POST":
        form = ProdottoForm(request.POST)
        if form.is_valid():
            form.save()  # INSERT INTO prodotti_prodotto ...
            return redirect("prodotti:lista")  # evita il reinvio del form al refresh
    else:
        form = ProdottoForm()
    return render(request, "prodotti/form.html", {"form": form, "titolo": "Nuovo prodotto"})


def modifica(request, pk):
    # UPDATE: SELECT del record (404 se non esiste), poi UPDATE al salvataggio
    prodotto = get_object_or_404(Prodotto, pk=pk)
    if request.method == "POST":
        # instance=prodotto fa sì che save() esegua UPDATE invece di INSERT
        form = ProdottoForm(request.POST, instance=prodotto)
        if form.is_valid():
            form.save()
            return redirect("prodotti:lista")
    else:
        form = ProdottoForm(instance=prodotto)  # form precompilato
    return render(request, "prodotti/form.html", {"form": form, "titolo": "Modifica prodotto"})


def elimina(request, pk):
    # DELETE: GET chiede conferma, POST esegue DELETE FROM ... WHERE id = pk
    prodotto = get_object_or_404(Prodotto, pk=pk)
    if request.method == "POST":
        prodotto.delete()
        return redirect("prodotti:lista")
    return render(request, "prodotti/conferma_elimina.html", {"prodotto": prodotto})
