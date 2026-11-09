from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

        self._lista_libri = []
        self._lista_biblioteche = []

        # Popolo le liste di libri e biblioteche
        self.get_libri()
        self.get_biblioteche()

        self._dict_libri = {}
        self._dict_biblioteche = {}

        for biblioteca in self._lista_biblioteche:
            self._dict_biblioteche[biblioteca.id] = biblioteca

        for libro in self._lista_libri:
            self._dict_libri[libro.id] = libro
            # Aggiungiamo un attributo in più agli oggetti di tipo Libro, contenente il riferimento all'oggetto Biblioteca in cui è contenuto il libro
            libro.biblioteca = self._dict_biblioteche[libro.id_biblioteca]





    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        # return self._libro_dao.get_libri_filtrati(biblioteca, genere)
        risultato = []

        for libro in self._lista_libri:
            if (libro.genere == genere or genere is None) and (libro.biblioteca.nome == biblioteca or biblioteca is None):
                risultato.append(libro)

        return risultato


    def get_libri(self):
        """Restituisce la lista di tutti i generi."""
        libro_dao = LibroDAO()

        if len(self._lista_libri) == 0:
            self._lista_libri = libro_dao.get_libri()
        else:
            pass
        return self._lista_libri


    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        biblioteche_dao = BibliotecaDAO()

        if len(self._lista_biblioteche) == 0:
            self._lista_biblioteche = biblioteche_dao.get_biblioteche()
        else:
            pass
        return self._lista_biblioteche