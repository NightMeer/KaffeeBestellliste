import init

def create(shema):
    if shema == 'mysql':
        try:
            init.dbcursor.execute(
                "CREATE TABLE Kaffeetemp ("
                "Kaffeetemp_ID  INT NOT NULL AUTO_INCREMENT, "
                "Hersteller VARCHAR(255) NOT NULL, "
                "Name VARCHAR(255) NOT NULL, "
                "Herkunft VARCHAR(255) NOT NULL, "
                "Anbauart VARCHAR(255) NOT NULL, "
                "Besonderheit VARCHAR(255) NOT NULL, "
                "Geschmacksprofil VARCHAR(255) NOT NULL, "
                "Preis_1000g VARCHAR(255) NOT NULL, "
                "Preis_500g VARCHAR(255) NOT NULL, "
                "Preis_250g VARCHAR(255) NOT NULL, "
                "Preis_100g VARCHAR(255) NOT NULL, "
                "PRIMARY KEY (Kaffeetemp_ID)"
                ")"
            )
        except Exception as e:
            print(e)
            print("Could not create Table Einkaufswagen")
    elif shema == 'sqlite':
        try:
            init.dbcursor.execute(
                "CREATE TABLE Kaffeetemp ("
                "Kaffeetemp_ID integer primary key autoincrement, "
                "Hersteller VARCHAR(255) NOT NULL, "
                "Name VARCHAR(255) NOT NULL, "
                "Herkunft VARCHAR(255) NOT NULL, "
                "Anbauart VARCHAR(255) NOT NULL, "
                "Besonderheit VARCHAR(255) NOT NULL, "
                "Geschmacksprofil VARCHAR(255) NOT NULL, "
                "Preis_1000g VARCHAR(255) NOT NULL, "
                "Preis_500g VARCHAR(255) NOT NULL, "
                "Preis_250g VARCHAR(255) NOT NULL, "
                "Preis_100g VARCHAR(255) NOT NULL"
                ")"
            )
        except Exception as e:
            print(e)
            print("Could not create Table Kaffeetemp")

def insert(hersteller, name, herkunft, anbauart, besonderheit, geschmacksprofil, preis_1000g, preis_500g, preis_250g, preis_100g):
    hersteller = "'" + hersteller + "'"
    name = "'" + name + "'"
    herkunft = "'" + herkunft + "'"
    anbauart = "'" + anbauart + "'"
    besonderheit = "'" + besonderheit + "'"
    geschmacksprofil = "'" + geschmacksprofil + "'"
    preis_1000g = "'" + preis_1000g + "'"
    preis_500g = "'" + preis_500g + "'"
    preis_250g = "'" + preis_250g + "'"
    preis_100g = "'" + preis_100g + "'"

    try:
        init.dbcursor.execute(
            "INSERT INTO Kaffeetemp (Hersteller, Name, Herkunft, Anbauart, Besonderheit, Geschmacksprofil, Preis_1000g, Preis_500g, Preis_250g, Preis_100g) VALUES (" + hersteller + "," + name + "," + herkunft + "," + anbauart + "," + besonderheit + "," + geschmacksprofil + "," + preis_1000g + "," + preis_500g + "," + preis_250g + "," + preis_100g + ")"
        )
        init.db.commit()
    except Exception as e:
        print(e)
        print("Could not insert into Kaffeetemp")

    print("Kaffeetemp inserted successfully")

def get_all():
    init.dbcursor.execute("SELECT * FROM Kaffeetemp")
    result = init.dbcursor.fetchall()
    return result

def get_by_id(id):
    init.dbcursor.execute("SELECT * FROM Kaffeetemp WHERE Kaffeetemp_ID = " + id)
    result = init.dbcursor.fetchall()
    return result[0]

def update(id, hersteller, name, herkunft, anbauart, besonderheit, geschmacksprofil, preis_1000g, preis_500g, preis_250g, preis_100g):
    id = "'" + id + "'"
    hersteller = "'" + hersteller + "', "
    name = "'" + name + "', "
    herkunft = "'" + herkunft + "', "
    anbauart = "'" + anbauart + "', "
    besonderheit = "'" + besonderheit + "', "
    geschmacksprofil = "'" + geschmacksprofil + "', "
    preis_1000g = "'" + preis_1000g + "', "
    preis_500g = "'" + preis_500g + "', "
    preis_250g = "'" + preis_250g + "', "
    preis_100g = "'" + preis_100g + "' "

    try:
        init.dbcursor.execute(
           "UPDATE Kaffeetemp SET Hersteller = " + hersteller + "Name = " + name + "Herkunft = " + herkunft + "Anbauart = " + anbauart + "Besonderheit = " + besonderheit + "Geschmacksprofil = " + geschmacksprofil + "Preis_1000g = " + preis_1000g + "Preis_500g = " + preis_500g + "Preis_250g = " + preis_250g + "Preis_100g = " + preis_100g + "WHERE Kaffeetemp_ID = " + id
        )
        init.db.commit()
    except Exception as e:
        print(e)
        print("Could not update Kaffeetemp")

def drop():
    try:
        init.dbcursor.execute("DROP TABLE Kaffeetemp")
    except Exception as e:
        print(e)
        print("Could not delete Table Kaffeetemp")

def delete_by_id(id):
    try:
        init.dbcursor.execute(
            "DELETE FROM Kaffeetemp WHERE Kaffeetemp_ID = " + id
        )
        init.db.commit()
    except Exception as e:
        print(e)
        print("Could not insert into Kaffeetemp")

def delete():
    try:
        init.dbcursor.execute("DELETE FROM Kaffeetemp")
    except Exception as e:
        print(e)
        print("Could not delete Table Kaffeetemp")