import init

def create(shema):
    if shema == 'mysql':
        try:
            init.dbcursor.execute(
                "CREATE TABLE Benutzer ("
                "Benutzer_ID INT NOT NULL AUTO_INCREMENT, "
                "Vorname VARCHAR(255) NOT NULL, "
                "Nachname VARCHAR(255) NOT NULL, "
                "Email VARCHAR(255) NOT NULL, "
                "Passwort VARCHAR(255) NOT NULL, "
                "Adresse VARCHAR(255) NOT NULL, "
                "Admin INT, "
                "UNIQUE (Email) ,"
                "PRIMARY KEY (Benutzer_ID)"
                ")"
            )
        except Exception as e:
            print(e)
            print("Could not create Table Einkaufswagen")
    elif shema == 'sqlite':
        try:
            init.dbcursor.execute(
                "CREATE TABLE Benutzer ("
                "Benutzer_ID integer primary key autoincrement, "
                "Vorname VARCHAR(255) NOT NULL, "
                "Nachname VARCHAR(255) NOT NULL, "
                "Email VARCHAR(255) NOT NULL, "
                "Passwort VARCHAR(255) NOT NULL, "
                "Adresse VARCHAR(255) NOT NULL, "
                "Admin INT, "
                "UNIQUE (Email)"
                ")"
            )
        except Exception as e:
            print(e)
            print("Could not create Table Kaffee")

def insert(vorname, nachname, email, passwort, adresse, admin):
    vorname = "'" + vorname + "'"
    nachname = "'" + nachname + "'"
    email = "'" + email + "'"
    passwort = "'" + passwort + "'"
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

def update(id, vorname = None, nachname = None, email = None, passwort = None, adresse = None, admin = None):
    if vorname:
        try:
            init.dbcursor.execute(
                "UPDATE Benutzer SET Vorname = '" + vorname + "' WHERE Benutzer_ID = " + str(id)
            )
            init.db.commit()
        except Exception as e:
            print(e)
            print("Could not update Benutzer")

    if nachname:
        try:
            init.dbcursor.execute(
                "UPDATE Benutzer SET Nachname = '" + nachname + "' WHERE Benutzer_ID = " + str(id)
            )
            init.db.commit()
        except Exception as e:
            print(e)
            print("Could not update Benutzer")

    if email:
        try:
            init.dbcursor.execute(
                "UPDATE Benutzer SET Email = '" + email + "' WHERE Benutzer_ID = " + str(id)
            )
            init.db.commit()
        except Exception as e:
            print(e)
            print("Could not update Benutzer")

    if passwort:
        try:
            init.dbcursor.execute(
                "UPDATE Benutzer SET Passwort = '" + passwort + "' WHERE Benutzer_ID = " + str(id)
            )
            init.db.commit()
        except Exception as e:
            print(e)
            print("Could not update Benutzer")

    if adresse:
        try:
            init.dbcursor.execute(
                "UPDATE Benutzer SET Adresse = '" + adresse + "' WHERE Benutzer_ID = " + str(id)
            )
            init.db.commit()
        except Exception as e:
            print(e)
            print("Could not update Benutzer")

    if admin:
        try:
            init.dbcursor.execute(
                "UPDATE Benutzer SET Admin = '" + admin + "' WHERE Benutzer_ID = " + str(id)
            )
            init.db.commit()
        except Exception as e:
            print(e)
            print("Could not update Benutzer")


def get_by_email(email):
    email = "'" + email + "'"

    init.dbcursor.execute("SELECT * FROM Benutzer WHERE email = " + email)
    result = init.dbcursor.fetchall()


    return result[0]

def get_by_id(id):
    init.dbcursor.execute("SELECT * FROM Benutzer WHERE Benutzer_ID = " + id)
    result = init.dbcursor.fetchall()

    return result[0]

def get_all():
    try:
        init.dbcursor.execute("SELECT * FROM Benutzer")
    except Exception as e:
        print(e)
        print("No Table Found")
        return 0
    result = init.dbcursor.fetchall()
    return result

def drop():
    try:
        init.dbcursor.execute("DROP TABLE Benutzer")
    except Exception as e:
        print(e)
        print("Could not delete Table Benutzer")

def delete_by_id(id):
    try:
        init.dbcursor.execute(
            "DELETE FROM Benutzer WHERE Benutzer_ID = " + id
        )
        init.db.commit()
    except Exception as e:
        print(e)
        print("Could not insert into Kaffee")

def delete():
    try:
        init.dbcursor.execute("DELETE FROM Benutzer")
    except Exception as e:
        print(e)
        print("Could not delete Table Benutzer")

