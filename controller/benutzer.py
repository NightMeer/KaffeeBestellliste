import models.benutzer
import functions


def fill():
    for x in range(10):
        vorname = functions.string_generator()
        nachname = functions.string_generator()
        email = vorname + "." + nachname + "@example.com"
        passwort = functions.get_hash(functions.string_generator())
        adresse = functions.string_generator()
        admin = "0"

        models.benutzer.insert(vorname, nachname, email, passwort, adresse, admin)

    return 1

def dbexist():
    if models.benutzer.get_all():
        return 1
    else:
        return 0

def update(id, vorname = None, nachname = None, email = None, adresse = None, passwort = None, admin = None):

    if vorname:
        vorname = functions.sql_escape(vorname)
        models.benutzer.update(id=id, vorname=vorname)
    if nachname:
        nachname = functions.sql_escape(nachname)
        models.benutzer.update(id=id, nachname=nachname)
    if email:
        email = functions.sql_escape(email)
        models.benutzer.update(id=id, email=email)
    if adresse:
        adresse = functions.sql_escape(adresse)
        models.benutzer.update(id=id, adresse=adresse)
    if passwort:
        models.benutzer.update(id=id, passwort=passwort)
    if admin:
        admin = functions.sql_escape(admin)
        models.benutzer.update(id=id, admin=admin)

    return 0

def get_by_id(id):
    return models.benutzer.get_by_id(id)

def get_by_email(email):
    return models.benutzer.get_by_email(email)

def get_all():
    return models.benutzer.get_all()

def insert(vorname, nachname, email, passwort, adresse, admin):
    vorname = functions.sql_escape(vorname)
    nachname = functions.sql_escape(nachname)
    email = functions.sql_escape(email)
    passwort = functions.sql_escape(passwort)
    passwort = functions.get_hash(passwort)
    adresse = functions.sql_escape(adresse)
    admin = functions.sql_escape(admin)

    models.benutzer.insert(vorname, nachname, email, passwort, adresse, admin)

def delete_by_id(id):
    return models.benutzer.delete_by_id(id)