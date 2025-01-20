from flask import session

import functions
import init

def fill():
    for x in range(10):
        vorname = functions.string_generator()
        nachname = functions.string_generator()
        email = vorname + "." + nachname + "@example.com"
        passwort = functions.get_hash(functions.string_generator())
        adresse = functions.string_generator()
        admin = "0"

        vorname = "'" + vorname + "'"
        nachname = "'" + nachname + "'"
        email = "'" + email + "'"
        passwort = "'" + passwort + "'"
        adresse = "'" + adresse + "'"
        admin = "'" + admin + "'"

        try:
            init.dbcursor.execute(
                "INSERT INTO Benutzer (Vorname, Nachname, Email, Passwort, Adresse, Admin) VALUES (" + vorname + "," + nachname + "," + email + "," + passwort + "," + adresse + "," + admin +")"
            )
            init.db.commit()
        except Exception as e:
            print(e)
            print("Could not insert into Benutzer")

def insert(vorname, nachname, email, passwort, adresse, admin):

    vorname = functions.sql_escape(vorname)
    nachname = functions.sql_escape(nachname)
    email = functions.sql_escape(email)
    passwort = functions.sql_escape(passwort)
    adresse = functions.sql_escape(adresse)
    admin = functions.sql_escape(admin)

    vorname = "'" + vorname + "'"
    nachname = "'" + nachname + "'"
    email = "'" + email + "'"
    passwort = "'" + functions.get_hash(passwort) + "'"
    adresse = "'" + adresse + "'"
    admin = "'" + admin + "'"

    try:
        init.dbcursor.execute(
            "INSERT INTO Benutzer (Vorname, Nachname, Email, Passwort, Adresse, Admin) VALUES (" + vorname + "," + nachname + "," + email + "," + passwort + "," + adresse + "," + admin + ")"
        )
        init.db.commit()
    except Exception as e:
        print(e)
        print("Could not insert into Benutzer")

    print("Benutzer inserted successfully")

def get_all():
    init.dbcursor.execute("SELECT * FROM Benutzer")
    result = init.dbcursor.fetchall()
    return result

def get_by_id(id):
    init.dbcursor.execute("SELECT Vorname, Nachname, Email, Adresse, Admin FROM Benutzer WHERE Benutzer_ID = " + id)
    result = init.dbcursor.fetchall()

    return result[0]

def loeschen(id):
    if session.get('id') != id:
        try:
            print("del")
            init.dbcursor.execute(
                "DELETE FROM Benutzer WHERE Benutzer_ID = " + id
            )
            init.db.commit()
        except Exception as e:
            print(e)
            print("Could not insert into Kaffee")

def update(id, vorname, nachname, email, passwort, adresse, admin):

    sql = "UPDATE Benutzer SET "

    vorname = functions.sql_escape(vorname)
    vorname = "'" + vorname + "', "
    sql = sql + "Vorname = " + vorname
    nachname = functions.sql_escape(nachname)
    nachname = "'" + nachname + "', "
    sql = sql + "Nachname = " + nachname
    if email != "":
        email = functions.sql_escape(email)
        email = "'" + email + "', "
        sql = sql + "Email = " + email
    if passwort != "":
        passwort = functions.sql_escape(passwort)
        passwort = "'" + passwort + "', "
        sql = sql + "Passwort = " + passwort
    adresse = functions.sql_escape(adresse)
    adresse = "'" + adresse + "', "
    sql = sql + "Adresse = " + adresse

    admin = functions.sql_escape(admin)
    admin = "'" + admin + "' "
    sql = sql + "Admin = " + admin

    sql = sql + "WHERE Benutzer_ID = " + id

    try:
        init.dbcursor.execute(
            sql
        )
        init.db.commit()
    except Exception as e:
        print(e)
        print("Could not update Benutzer")

    return 1