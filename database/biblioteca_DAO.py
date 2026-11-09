from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_biblioteche(self):
        biblioteche = []

        conn = DBConnect.get_connection()
        if conn is not None:
            query = "SELECT id, nome, indirizzo FROM biblioteca"
            cursor = conn.cursor()
            cursor.execute(query)

            righe = cursor.fetchall()
            cursor.close()
            conn.close()

            for riga in righe:
                biblioteca = Biblioteca(*riga)
                biblioteche.append(biblioteca)

            return biblioteche




