import functions
import init
import kaffee as k
from benutzer import loeschen


def get_all():
    init.dbcursor.execute("SELECT * FROM Einkaufswagen")
    result = init.dbcursor.fetchall()
    return result

def get_all_user_id(id):
    init.dbcursor.execute("SELECT * FROM Einkaufswagen WHERE Benutzer_ID = " + id)
    result = init.dbcursor.fetchall()
    return result

def get_all_user_id_formated(id):

    einkaufswagen = get_all_user_id(id)

    print(type(einkaufswagen))

    result = []

    for data in einkaufswagen:
        kaffee_id = data[2]
        gramm = data[3]
        menge = data[4]

        kaffee = k.get_by_id(kaffee_id) + (gramm, menge)

        result.append(kaffee)
    return result

def insert(benutzer_ID, kaffee_ID, menge, gramm):
    benutzer_ID = functions.sql_escape(benutzer_ID)
    kaffee_ID = functions.sql_escape(kaffee_ID)
    if menge == "0":
        menge = "1"

    print(menge)

    menge = functions.sql_escape(menge)
    gramm = functions.sql_escape(gramm)
    gramm = "'" + gramm + "'"


    init.dbcursor.execute(
        "SELECT * FROM Einkaufswagen WHERE Benutzer_ID = " + benutzer_ID + " AND Kaffee_ID = " + kaffee_ID + " AND Gramm = " + gramm
    )
    result = init.dbcursor.fetchone()

    benutzer_ID = "'" + benutzer_ID + "'"
    kaffee_ID = "'" + kaffee_ID + "'"
    mengeinsert = "'" + menge + "'"




    try:
        if result == None:
            init.dbcursor.execute(
                "INSERT INTO Einkaufswagen (Benutzer_ID, Kaffee_ID, Menge, Gramm) VALUES (" + benutzer_ID + "," + kaffee_ID + "," + mengeinsert + "," + gramm + ")"
            )
            init.db.commit()
        else:
            mengeinsert = int(menge) + int(result[3]) # Menge
            init.dbcursor.execute(
                "UPDATE Einkaufswagen SET Menge = "+ str(mengeinsert) +" WHERE Einkaufswagen_ID = " + str(result[0])
            )
            init.db.commit()

            print(mengeinsert)
            print("Update")
    except Exception as e:
        print(e)
        print("Could not insert into Einkaufswagen")

    print("Bestellung hinzugefügt")

def update(benutzer_ID, kaffee_ID, menge, gramm):
    loeschen = 0

    benutzer_ID = functions.sql_escape(benutzer_ID)
    kaffee_ID = functions.sql_escape(kaffee_ID)
    menge = functions.sql_escape(menge)
    gramm = functions.sql_escape(gramm)
    gramm = "'" + gramm + "'"

    if menge == "0":
        loeschen = 1

    init.dbcursor.execute(
        "SELECT * FROM Einkaufswagen WHERE Benutzer_ID = " + benutzer_ID + " AND Kaffee_ID = " + kaffee_ID + " AND Gramm = " + gramm
    )
    result = init.dbcursor.fetchone()

    benutzer_ID = "'" + benutzer_ID + "'"
    kaffee_ID = "'" + kaffee_ID + "'"
    mengeinsert = "'" + menge + "'"



    try:
        if not loeschen:
            init.dbcursor.execute(
                "UPDATE Einkaufswagen SET Menge = " + str(mengeinsert) + " WHERE Einkaufswagen_ID = " + str(result[0])
            )
            init.db.commit()
        else:
            init.dbcursor.execute(
                "DELETE FROM Einkaufswagen WHERE Einkaufswagen_ID = " + str(result[0])
            )
            init.db.commit()

            print(mengeinsert)
            print("Löschenm")
    except Exception as e:
        print(e)
        print("Could not insert into Einkaufswagen")

    print("Bestellung SET")