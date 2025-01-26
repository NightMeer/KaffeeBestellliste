import os
import sqlite3
import mysql.connector

from dotenv import load_dotenv

import models.benutzer
import models.bewertung
import models.einkaufswagen
import models.kaffee
import models.kaffeetemp

import controller.kaffee
import controller.benutzer

load_dotenv()

HTML_LANG = os.environ.get("HTML_LANG", "de")
HTML_TITLE = os.environ.get("HTML_TITLE", "KaffeeBestellliste")
FLASK_SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "SECRET_KEY")
UPLOAD_FOLDER = os.environ.get("UPLOAD_PATH", "uploads")
ALLOWED_EXTENSIONS = {'txt', 'csv'}
DATABE_TYPE= os.environ.get("DATABE_TYPE", "sqlite")


def init_db():
    if os.environ.get("DATABASE_TYPE") == 'mysql':
        try:
            db = mysql.connector.connect(
                host=os.environ.get("MYSQL_HOST"),
                user=os.environ.get("MYSQL_USER"),
                password=os.environ.get("MYSQL_PASSWORD"),
                database=os.environ.get("MYSQL_DATABASE")
            )
            print("Connecting to MySQL database...")
        except Exception as e:
            print(e)
            print("Database connection failed.")
            exit()
    elif os.environ.get("DATABASE_TYPE") == "sqlite":
        print("Connecting to SQLite database...")
        db = sqlite3.connect('database.sqlite', check_same_thread=False)
    else:
        print("Unknown database type.")
        exit()

    print("Database initialized.")
    return db

def install():
    print("Installing...")

    models.benutzer.create(DATABE_TYPE)
    models.bewertung.create(DATABE_TYPE)
    models.einkaufswagen.create(DATABE_TYPE)
    models.kaffee.create(DATABE_TYPE)
    models.kaffeetemp.create(DATABE_TYPE)



def fill():
    controller.benutzer.fill()
    controller.kaffee.fill()

def delete():
    models.benutzer.drop()
    models.bewertung.drop()
    models.einkaufswagen.drop()
    models.kaffee.drop()
    models.kaffeetemp.drop()


def delete_kaffee():
    models.kaffee.delete()

def delete_einkaufswagen():
    models.einkaufswagen.delete()

db = init_db()
dbcursor = db.cursor()