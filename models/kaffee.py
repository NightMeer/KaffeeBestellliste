import init

def create(shema):
    if shema == 'mysql':
        try:
            init.dbcursor.execute(
                "CREATE TABLE Kaffee ("
                "Kaffee_ID  INT NOT NULL AUTO_INCREMENT, "
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
                "PRIMARY KEY (Kaffee_ID)"
                ")"
            )
        except Exception as e:
            print(e)
            print("Could not create Table Einkaufswagen")
    elif shema == 'sqlite':
        try:
            init.dbcursor.execute(
                "CREATE TABLE Kaffee ("
                "Kaffee_ID integer primary key autoincrement, "
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
            print("Could not create Table Kaffee")

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
            "INSERT INTO Kaffee (Hersteller, Name, Herkunft, Anbauart, Besonderheit, Geschmacksprofil, Preis_1000g, Preis_500g, Preis_250g, Preis_100g) VALUES (" + hersteller + "," + name + "," + herkunft + "," + anbauart + "," + besonderheit + "," + geschmacksprofil + "," + preis_1000g + "," + preis_500g + "," + preis_250g + "," + preis_100g + ")"
        )
        init.db.commit()
    except Exception as e:
        print(e)
        print("Could not insert into Kaffee")

    print("Kaffee inserted successfully")

def get_all():
    init.dbcursor.execute("SELECT * FROM Kaffee")
    result = init.dbcursor.fetchall()
    return result

def get_by_id(id):
    init.dbcursor.execute("SELECT * FROM Kaffee WHERE Kaffee_ID = " + id)
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
           "UPDATE Kaffee SET Hersteller = " + hersteller + "Name = " + name + "Herkunft = " + herkunft + "Anbauart = " + anbauart + "Besonderheit = " + besonderheit + "Geschmacksprofil = " + geschmacksprofil + "Preis_1000g = " + preis_1000g + "Preis_500g = " + preis_500g + "Preis_250g = " + preis_250g + "Preis_100g = " + preis_100g + "WHERE Kaffee_ID = " + id
        )
        init.db.commit()
    except Exception as e:
        print(e)
        print("Could not update Kaffee")

def drop():
    try:
        init.dbcursor.execute("DROP TABLE Kaffee")
    except Exception as e:
        print(e)
        print("Could not delete Table Kaffee")

def delete_by_id(id):
    try:
        init.dbcursor.execute(
            "DELETE FROM Kaffee WHERE Kaffee_ID = " + id
        )
        init.db.commit()
    except Exception as e:
        print(e)
        print("Could not insert into Kaffee")

def delete():
    try:
        init.dbcursor.execute("DELETE FROM Kaffee")
    except Exception as e:
        print(e)
        print("Could not delete Table Kaffee")