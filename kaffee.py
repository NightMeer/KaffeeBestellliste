import functions
import init



def get_all():
    init.dbcursor.execute("SELECT * FROM Kaffee")
    result = init.dbcursor.fetchall()
    return result

def insert(hersteller, name, herkunft, anbauart, besonderheit, geschmacksprofil, preis_1000g, preis_500g, preis_250g, preis_100g):
    hersteller = functions.sql_escape(hersteller)
    name = functions.sql_escape(name)
    herkunft = functions.sql_escape(herkunft)
    anbauart = functions.sql_escape(anbauart)
    besonderheit = functions.sql_escape(besonderheit)
    geschmacksprofil = functions.sql_escape(geschmacksprofil)
    preis_1000g = functions.sql_escape(preis_1000g)
    preis_500g = functions.sql_escape(preis_500g)
    preis_250g = functions.sql_escape(preis_250g)
    preis_100g = functions.sql_escape(preis_100g)

    preis_1000g = functions.geld_replace(preis_1000g)
    preis_500g = functions.geld_replace(preis_500g)
    preis_250g = functions.geld_replace(preis_250g)
    preis_100g = functions.geld_replace(preis_100g)

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

def get_by_id(id):
    init.dbcursor.execute("SELECT Kaffee_ID, Hersteller, Name, Herkunft, Anbauart, Besonderheit, Geschmacksprofil, Preis_1000g, Preis_500g, Preis_250g, Preis_100g FROM Kaffee WHERE Kaffee_ID = " + id)
    result = init.dbcursor.fetchall()
    print(result)
    return result[0]

def update(id, hersteller, name, herkunft, anbauart, besonderheit, geschmacksprofil, preis_1000g, preis_500g, preis_250g, preis_100g):
    sql = "UPDATE Kaffee SET "

    hersteller = functions.sql_escape(hersteller)
    hersteller = "'" + hersteller + "', "
    sql = sql + "Hersteller = " + hersteller

    herkunft = functions.sql_escape(herkunft)
    herkunft = "'" + herkunft + "', "
    sql = sql + "Herkunft = " + herkunft

    anbauart = functions.sql_escape(anbauart)
    anbauart = "'" + anbauart + "', "
    sql = sql + "Anbauart = " + anbauart

    besonderheit = functions.sql_escape(besonderheit)
    besonderheit = "'" + besonderheit + "', "
    sql = sql + "Besonderheit = " + besonderheit

    geschmacksprofil = functions.sql_escape(geschmacksprofil)
    geschmacksprofil = "'" + geschmacksprofil + "', "
    sql = sql + "Geschmacksprofil = " + geschmacksprofil


    preis_1000g = functions.geld_replace(preis_1000g)
    preis_1000g = functions.sql_escape(preis_1000g)
    preis_1000g = "'" + preis_1000g + "', "
    sql = sql + "Preis_1000g = " + preis_1000g

    preis_500g = functions.geld_replace(preis_500g)
    preis_500g = functions.sql_escape(preis_500g)
    preis_500g = "'" + preis_500g + "', "
    sql = sql + "Preis_500g = " + preis_500g

    preis_250g = functions.geld_replace(preis_250g)
    preis_250g = functions.sql_escape(preis_250g)
    preis_250g = "'" + preis_250g + "', "
    sql = sql + "Preis_250g = " + preis_250g

    preis_100g = functions.geld_replace(preis_100g)
    preis_100g = functions.sql_escape(preis_100g)
    preis_100g = "'" + preis_100g + "', "
    sql = sql + "Preis_100g = " + preis_100g

    name = functions.sql_escape(name)
    name = "'" + name + "'"
    sql = sql + "Name = " + name

    sql = sql + "WHERE Kaffee_ID = " + id

    try:
        init.dbcursor.execute(
            sql
        )
        init.db.commit()
    except Exception as e:
        print(e)
        print("Could not update Kaffee")

    return 1

def loeschen(id):
    try:
        init.dbcursor.execute(
            "DELETE FROM Kaffee WHERE Kaffee_ID = " + id
        )
        init.db.commit()
    except Exception as e:
        print(e)
        print("Could not insert into Kaffee")

def fill():
    for x in range(10):

        hersteller = functions.string_generator()
        name = functions.string_generator()
        herkunft = functions.string_generator()
        anbauart = functions.string_generator()
        besonderheit = functions.string_generator()
        geschmacksprofil = functions.string_generator()
        preis_1000g = functions.number_generator(4)
        preis_500g = functions.number_generator(4)
        preis_250g = functions.number_generator(4)
        preis_100g = functions.number_generator(4)

        preis_1000g = preis_1000g[:2] + "." + preis_1000g[2:]
        preis_500g = preis_500g[:2] + "." + preis_500g[2:]
        preis_250g = preis_250g[:2] + "." + preis_250g[2:]
        preis_100g = preis_100g[:2] + "." + preis_100g[2:]

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
                "INSERT INTO 'Kaffee' (Hersteller, Name, Herkunft, Anbauart, Besonderheit, Geschmacksprofil, Preis_1000g, Preis_500g, Preis_250g, Preis_100g) VALUES (" + hersteller + "," + name + "," + herkunft + "," + anbauart + "," + besonderheit + "," + geschmacksprofil + "," + preis_1000g + "," + preis_500g + "," + preis_250g + "," + preis_100g +")"
            )
            init.db.commit()
        except Exception as e:
            print(e)
            print("Could not insert into Kaffee")

