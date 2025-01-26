import init

def create(shema):
    if shema == 'mysql':
        try:
            init.dbcursor.execute(
                "CREATE TABLE Bestellung ("
                "Bestellung_ID  INT NOT NULL AUTO_INCREMENT, "
                "Benutzer_ID VARCHAR(255) NOT NULL, "
                "Kaffee_ID VARCHAR(255) NOT NULL, "
                "Menge VARCHAR(255) NOT NULL, "
                "Gramm VARCHAR(255) NOT NULL, "
                "PRIMARY KEY (Bestellung_ID)"
                ")"
            )
        except Exception as e:
            print(e)
            print("Could not create Table Bestellung")
    elif shema == 'sqlite':
        try:
            init.dbcursor.execute(
                "CREATE TABLE Bestellung ("
                "Bestellung_ID integer primary key autoincrement, "
                "Benutzer_ID VARCHAR(255) NOT NULL, "
                "Kaffee_ID VARCHAR(255) NOT NULL, "
                "Menge VARCHAR(255) NOT NULL, "
                "Gramm VARCHAR(255) NOT NULL"
                ")"
            )
        except Exception as e:
            print(e)
            print("Could not create Table Kaffee")

def insert(benutzer_ID, kaffee_ID, gramm, menge):
    benutzer_ID = "'" + benutzer_ID + "'"
    kaffee_ID = "'" + kaffee_ID + "'"
    menge = "'" + menge + "'"
    gramm = "'" + gramm + "'"

    try:
        init.dbcursor.execute(
            "INSERT INTO Bestellung (Benutzer_ID, Kaffee_ID, Menge, Gramm) VALUES (" + benutzer_ID + "," + kaffee_ID + "," + menge + "," + gramm + ")"
        )
        init.db.commit()
    except Exception as e:
        print(e)
        print("Could not insert into Benutzer")

def set_menge(id, menge):

    menge = "'" + str(menge) + "'"

    try:
        init.dbcursor.execute(
            "UPDATE Bestellung SET Menge = " + menge + "WHERE Bestellung_ID = " + str(id)
        )
        init.db.commit()
    except Exception as e:
        print(e)
        print("Could not insert into Benutzer")

def update(id, benutzer_ID, kaffee_ID, menge, gramm):
    id = "'" + id + "'"
    benutzer_ID = "'" + benutzer_ID + "', "
    kaffee_ID = "'" + kaffee_ID + "', "
    menge = "'" + menge + "', "
    gramm = "'" + gramm + "', "

    try:
        init.dbcursor.execute(
           "UPDATE Benutzer SET Benutzer_ID = " + benutzer_ID + "Kaffee_ID = " + kaffee_ID + "Menge = " + menge + "Gramm = " + gramm + "WHERE Bestellung_ID = " + id
        )
        init.db.commit()
    except Exception as e:
        print(e)
        print("Could not update Benutzer")

def get_all():
    init.dbcursor.execute("SELECT * FROM Bestellung")
    result = init.dbcursor.fetchall()
    return result

def get_all_by_user_id(id):
    init.dbcursor.execute("SELECT * FROM Bestellung WHERE Benutzer_ID = " + id)
    result = init.dbcursor.fetchall()
    return result

def get_id(id):
    init.dbcursor.execute("SELECT * FROM Bestellung WHERE Bestellung_ID = " + id)
    result = init.dbcursor.fetchall()
    return result

def get_by_kaffeeid_benutzerid_gramm(kaffeeid, benutzerid, gramm):
    kaffeeid = "'" + kaffeeid + "'"
    benutzerid = "'" + benutzerid + "'"
    gramm = "'" + gramm + "'"

    init.dbcursor.execute("SELECT * FROM Bestellung WHERE Kaffee_ID = " + kaffeeid + " AND Benutzer_ID = " + benutzerid + " AND Gramm = " + gramm)

    result = init.dbcursor.fetchall()

    if result == []:
        return None
    else:
        return result[0]

def drop():
    try:
        init.dbcursor.execute("DROP TABLE Bestellung")
    except Exception as e:
        print(e)
        print("Could not delete Table Benutzer")

def delete():
    try:
        init.dbcursor.execute("DELETE FROM Bestellung")
    except Exception as e:
        print(e)
        print("Could not delete Table Benutzer")