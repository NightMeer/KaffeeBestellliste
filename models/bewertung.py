import init

def create(shema):
    if shema == 'mysql':
        try:
            init.dbcursor.execute(
                "CREATE TABLE Bewertung ("
                "Bewertung_ID  INT NOT NULL AUTO_INCREMENT, "
                "Benutzer_ID VARCHAR(255) NOT NULL, "
                "Kaffee_ID VARCHAR(255) NOT NULL, "
                "Bewertung VARCHAR(255) NOT NULL, "
                "Bewertung_Text VARCHAR(255) NOT NULL, "
                "PRIMARY KEY (Bewertung_ID)"
                ")"
            )
        except Exception as e:
            print(e)
            print("Could not create Table Einkaufswagen")
    elif shema == 'sqlite':
        try:
            init.dbcursor.execute(
                "CREATE TABLE Bewertung ("
                "Bewertung_ID integer primary key autoincrement, "
                "Benutzer_ID VARCHAR(255) NOT NULL, "
                "Kaffee_ID VARCHAR(255) NOT NULL, "
                "Bewertung VARCHAR(255) NOT NULL, "
                "Bewertung_Text VARCHAR(255) NOT NULL"
                ")"
            )
        except Exception as e:
            print(e)
            print("Could not create Table Kaffee")

def insert(benutzer_id, kaffee_id, bewertung, bewertung_text):
    benutzer_id = "'" + benutzer_id + "'"
    kaffee_id = "'" + kaffee_id + "'"
    bewertung = "'" + bewertung + "'"
    bewertung_text = "'" + bewertung_text + "'"

    try:
        init.dbcursor.execute(
            "INSERT INTO Bewertung (Benutzer_ID, Kaffee_ID, Bewertung_Text) VALUES (" + benutzer_id + "," + kaffee_id + "," + bewertung + "," + bewertung_text + ")"
        )
        init.db.commit()
    except Exception as e:
        print(e)
        print("Could not insert into Benutzer")

    print("Benutzer inserted successfully")

def drop():
    try:
        init.dbcursor.execute("DROP TABLE Bewertung")
    except Exception as e:
        print(e)
        print("Could not delete Table Benutzer")

def delete():
    try:
        init.dbcursor.execute("DELETE FROM Bewertung")
    except Exception as e:
        print(e)
        print("Could not delete Table Benutzer")