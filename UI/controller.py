from asyncio.windows_events import NULL

import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_biblioteche(self):
        self._view.dd_biblioteca.options.clear()

        lista_biblioteche = self._model.get_biblioteche()

        self._view.dd_biblioteca.options.append(ft.dropdown.Option(text="Nessun filtro"))
        for bib in lista_biblioteche:
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(bib.nome))

    def popola_genere_libri(self):
        self._view.dd_genere.options.clear()

        generi = []     # lista di generi per memorizzare i generi già inseriti nella dropdown senza duplicarli
        libri = self._model.get_libri()

        self._view.dd_genere.options.append(ft.dropdown.Option(text="Nessun filtro"))
        for libro in libri:
            if libro.genere not in generi:
                generi.append(libro.genere)
                self._view.dd_genere.options.append(ft.dropdown.Option(libro.genere))

    # CALLBACKS DROPDOWN
    def salva_filtro_biblioteca(self):
        valore = self._view.dd_biblioteca.value
        if valore == "Nessun filtro":   # se viene selezionato "Nessun filtro" il valore deve essere None
            valore = None
        else:
            pass
        self.biblioteca_selezionata = valore

    def salva_filtro_genere(self):
        valore = self._view.dd_genere.value
        if valore == "Nessun filtro":
            valore = None
        else:
            pass
        self.genere_selezionato = valore

    # AZIONE: MOSTRA LIBRI
    def mostra_libri_filtrati(self, e):
        self._view.lista_libri.controls.clear()

        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)
        if len(libri) > 0:
            for libro in libri:
                self._view.lista_libri.controls.append(ft.Text(f"{libro}"))
        else:
            self._view.show_alert(f"Non sono presenti libri di genere '{self.genere_selezionato}' presso la {self.biblioteca_selezionata}")
