import os
import sqlite3
import mysql.connector
import benutzer, kaffee

from dotenv import load_dotenv

load_dotenv()

HTML_LANG = os.environ.get("HTML_LANG", "de")
HTML_TITLE = os.environ.get("HTML_TITLE", "KaffeeBestellliste")
FLASK_SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "SECRET_KEY")

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
    if os.environ.get("DATABASE_TYPE") == 'mysql':
        try:
            dbcursor.execute(
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
            print("Could not create Table Benutzer")

        try:
            dbcursor.execute(
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

        try:
            dbcursor.execute(
                "CREATE TABLE Einkaufswagen ("
                "Einkaufswagen_ID  INT NOT NULL AUTO_INCREMENT, "
                "Benutzer_ID VARCHAR(255) NOT NULL, "
                "Kaffee_ID VARCHAR(255) NOT NULL, "
                "Menge VARCHAR(255) NOT NULL, "
                "Gramm VARCHAR(255) NOT NULL, "
                "PRIMARY KEY (Einkaufswagen_ID)"
                ")"
            )
        except Exception as e:
            print(e)
            print("Could not create Table Einkaufswagen")

        try:
            dbcursor.execute(
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
            print("Could not create Table Bewertung")

    elif os.environ.get("DATABASE_TYPE") == 'sqlite':
        try:
            dbcursor.execute(
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
            print("Could not create Table Benutzer")

        try:
            dbcursor.execute(
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

        try:
            dbcursor.execute(
                "CREATE TABLE Einkaufswagen ("
                "Einkaufswagen_ID integer primary key autoincrement, "
                "Benutzer_ID VARCHAR(255) NOT NULL, "
                "Kaffee_ID VARCHAR(255) NOT NULL, "
                "Menge VARCHAR(255) NOT NULL, "
                "Gramm VARCHAR(255) NOT NULL"
                ")"
            )
        except Exception as e:
            print(e)
            print("Could not create Table Einkaufswagen")

        try:
            dbcursor.execute(
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
            print("Could not create Table Bewertung")

def fill():
    benutzer.fill()
    kaffee.fill()

def delete():
    try:
        dbcursor.execute("DROP TABLE Benutzer")
    except Exception as e:
        print(e)
        print("Could not delete Table Benutzer")
    try:
        dbcursor.execute("DROP TABLE Kaffee")
    except Exception as e:
        print(e)
        print("Could not delete Table Kaffee")
    try:
        dbcursor.execute("DROP TABLE Einkaufswagen")
    except Exception as e:
        print(e)
        print("Could not delete Table Einkaufswagen")
    try:
        dbcursor.execute("DROP TABLE Bewertung")
    except Exception as e:
        print(e)
        print("Could not delete Table Bewertung")

def delete_kaffee():
    try:
        dbcursor.execute("DELETE FROM Kaffee")
    except Exception as e:
        print(e)
        print("Could not delete Table Benutzer")

db = init_db()
dbcursor = db.cursor()