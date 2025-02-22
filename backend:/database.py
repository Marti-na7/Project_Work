import sqlite3 

 

def create_database(): 

    conn = sqlite3.connect("database.db") 

    cursor = conn.cursor() 

 

    # Creazione tabella utenti 

    cursor.execute(''' 

        CREATE TABLE IF NOT EXISTS users ( 

            codice_fiscale TEXT PRIMARY KEY, 

            nome TEXT NOT NULL, 

            cognome TEXT NOT NULL, 

            email TEXT UNIQUE NOT NULL, 

            telefono TEXT NOT NULL, 

            data_nascita TEXT NOT NULL, 

            luogo_nascita TEXT NOT NULL 

        ) 

    ''') 

 

    # Creazione tabella prenotazioni 

    cursor.execute(''' 

        CREATE TABLE IF NOT EXISTS appointments ( 

            id INTEGER PRIMARY KEY AUTOINCREMENT, 

            codice_fiscale TEXT NOT NULL, 

            servizio TEXT NOT NULL, 

            data_appuntamento TEXT NOT NULL, 

            ora TEXT NOT NULL, 

            consulente TEXT NOT NULL, 

            stato TEXT DEFAULT "Confermato", 

            FOREIGN KEY (codice_fiscale) REFERENCES users (codice_fiscale) 

        ) 

    ''') 

 

    conn.commit() 

    conn.close() 

 

if __name__ == "__main__": 

    create_database() 
