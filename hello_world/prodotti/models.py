"""
LIVELLO DATI (nessun SQL scritto a mano).

Ogni classe Model corrisponde a una tabella. Django genera l'SQL
(CREATE TABLE, INSERT, SELECT, UPDATE, DELETE) a partire da questa definizione:
- `makemigrations` crea il file di migrazione dai modelli
- `migrate` esegue l'SQL sul db sqlite3 (db.sqlite3)
"""
from django.db import models


class Prodotto(models.Model):
    # id: chiave primaria autoincrementale, aggiunta automaticamente da Django
    nome = models.CharField(max_length=100)
    prezzo = models.DecimalField(max_digits=8, decimal_places=2)
    colore = models.CharField(max_length=30)
    capacita = models.PositiveIntegerField(help_text="Capacità (es. in GB o litri)")

    def __str__(self):
        # Rappresentazione testuale (usata ad es. nell'admin e nella conferma di eliminazione)
        return self.nome
