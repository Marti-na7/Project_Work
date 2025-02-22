from flask import Flask, request, jsonify 

from flask_cors import CORS 

import sqlite3 

 

app = Flask(__name__) 

CORS(app) 

 

# Funzione per connettersi al database 

def get_db_connection(): 

    conn = sqlite3.connect("database.db") 

    conn.row_factory = sqlite3.Row 

    return conn 

 

# Registrazione utente 

@app.route("/register", methods=["POST"]) 

def register(): 

    data = request.get_json() 

    conn = get_db_connection() 

    cursor = conn.cursor() 

 

    try: 

        cursor.execute(''' 

            INSERT INTO users (codice_fiscale, nome, cognome, email, telefono, data_nascita, luogo_nascita) 

            VALUES (?, ?, ?, ?, ?, ?, ?) 

        ''', (data["codice_fiscale"], data["nome"], data["cognome"], data["email"], data["telefono"], data["data_nascita"], data["luogo_nascita"])) 

        conn.commit() 

        return jsonify({"message": "Registrazione avvenuta con successo"}), 201 

    except sqlite3.IntegrityError: 

        return jsonify({"error": "Codice fiscale o email già registrati"}), 400 

    finally: 

        conn.close() 

 

# Prenotazione appuntamento 

@app.route("/book", methods=["POST"]) 

def book_appointment(): 

    data = request.get_json() 

    conn = get_db_connection() 

    cursor = conn.cursor() 

 

    cursor.execute(''' 

        INSERT INTO appointments (codice_fiscale, servizio, data_appuntamento, ora, consulente) 

        VALUES (?, ?, ?, ?, ?) 

    ''', (data["codice_fiscale"], data["servizio"], data["data_appuntamento"], data["ora"], data["consulente"])) 

     

    conn.commit() 

    conn.close() 

    return jsonify({"message": "Prenotazione avvenuta con successo"}), 201 

 

# Visualizzare le prenotazioni di un utente 

@app.route("/appointments/<codice_fiscale>", methods=["GET"]) 

def get_appointments(codice_fiscale): 

    conn = get_db_connection() 

    cursor = conn.cursor() 

 

    cursor.execute("SELECT * FROM appointments WHERE codice_fiscale = ?", (codice_fiscale,)) 

    appointments = cursor.fetchall() 

 

    conn.close() 

    return jsonify([dict(row) for row in appointments]) 

 

if __name__ == "__main__": 

    app.run(debug=True) 
