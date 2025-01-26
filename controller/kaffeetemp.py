import models.kaffeetemp
import functions


def fill():
    for x in range(10):
        hersteller = functions.string_generator()
        name = functions.string_generator()
        herkunft = functions.string_generator()
        anbauart = functions.string_generator()
        besonderheit = functions.string_generator()
        geschmacksprofil = functions.string_generator()
        preis_1000g = functions.number_generator(2) + "." + functions.number_generator(2)
        preis_500g = functions.number_generator(2) + "." + functions.number_generator(2)
        preis_250g = functions.number_generator(2) + "." + functions.number_generator(2)
        preis_100g = functions.number_generator(2) + "." + functions.number_generator(2)

        models.kaffeetemp.insert(hersteller, name, herkunft, anbauart, besonderheit, geschmacksprofil, preis_1000g, preis_500g, preis_250g, preis_100g)

    return 1

def get_all():
    return models.kaffeetemp.get_all()

def get_by_id(id):
    return models.kaffeetemp.get_by_id(id)

def loeschen(id):
    return models.kaffeetemp.delete_by_id(id)

def update(id, hersteller, name, herkunft, anbauart, besonderheit, geschmacksprofil, preis_1000g, preis_500g, preis_250g, preis_100g):
    hersteller = functions.sql_escape(hersteller)
    name = functions.sql_escape(name)
    herkunft = functions.sql_escape(herkunft)
    anbauart = functions.sql_escape(anbauart)
    besonderheit = functions.sql_escape(besonderheit)
    geschmacksprofil = functions.sql_escape(geschmacksprofil)
    preis_1000g = functions.geld_replace(preis_1000g)
    preis_500g = functions.geld_replace(preis_500g)
    preis_250g = functions.geld_replace(preis_250g)
    preis_100g = functions.geld_replace(preis_100g)

    models.kaffeetemp.update(id, hersteller, name, herkunft, anbauart, besonderheit, geschmacksprofil, preis_1000g, preis_500g, preis_250g, preis_100g)

def insert(hersteller, name, herkunft, anbauart, besonderheit, geschmacksprofil, preis_1000g, preis_500g, preis_250g, preis_100g):

    hersteller = functions.sql_escape(hersteller)
    name = functions.sql_escape(name)
    herkunft = functions.sql_escape(herkunft)
    anbauart = functions.sql_escape(anbauart)
    besonderheit = functions.sql_escape(besonderheit)
    geschmacksprofil = functions.sql_escape(geschmacksprofil)
    preis_1000g = functions.geld_replace(preis_1000g)
    preis_500g = functions.geld_replace(preis_500g)
    preis_250g = functions.geld_replace(preis_250g)
    preis_100g = functions.geld_replace(preis_100g)


    models.kaffeetemp.insert(hersteller, name, herkunft, anbauart, besonderheit, geschmacksprofil, preis_1000g, preis_500g, preis_250g, preis_100g)
