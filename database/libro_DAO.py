from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    @staticmethod
    def get_libri():
        libri = []

        conn = DBConnect.get_connection()
        if conn is not None:
            query = "SELECT id, titolo, autore, genere, anno_pubblicazione, id_biblioteca FROM libro"
            cursor = conn.cursor()
            cursor.execute(query)

            righe = cursor.fetchall()
            cursor.close()
            conn.close()

            for riga in righe:
                libro = Libro(*riga)
                libri.append(libro)

            return libri
        else:
            print("No connessione")
            return None

    @staticmethod
    def get_libri_filtrati(biblioteca : str, genere: str):
        libri_filtrati = []

        conn = DBConnect.get_connection()
        if conn is not None:
            query = """SELECT l.id, titolo, autore, genere, anno_pubblicazione, id_biblioteca    
                        FROM libro l, biblioteca b 
                        WHERE l.id_biblioteca = b.id AND
                        b.nome = COALESCE(%s, b.nome) AND
                        l.genere = COALESCE(%s, l.genere)"""
            cursor = conn.cursor()
            cursor.execute(query, (biblioteca, genere))
            righe = cursor.fetchall()
            cursor.close()
            conn.close()

            for riga in righe:
                libro = Libro(*riga)
                libri_filtrati.append(libro)

            return libri_filtrati
        else:
            print("No connessione")
            return None


