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

        for bib in lista_biblioteche:
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(bib.nome))

    def popola_genere_libri(self):
        self._view.dd_genere.options.clear()

        generi = []
        libri = self._model.get_libri()

        for libro in libri:
            if libro.genere not in generi:
                generi.append(libro.genere)
                self._view.dd_genere.options.append(ft.dropdown.Option(libro.genere))

    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA LIBRI
    def mostra_libri_filtrati(self, e):
        self._view.lista_libri.controls.clear()

        libri = self._model.get_libri_filtrati(self._view.dd_biblioteca.value, self._view.dd_genere.value)
        for libro in libri:
            self._view.lista_libri.controls.append(ft.Text(f"{libro}"))
