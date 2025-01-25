import string
import random
import init
import hashlib
import re
from flask import session, abort


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def number_generator(size=6, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def string_generator(size=6, chars=string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

def check_hash(plain_text, hash):
    plain_text = plain_text.encode('utf-8')
    hash_object = hashlib.sha256(plain_text)
    hex_dig = hash_object.hexdigest()
    if hex_dig == hash:
        return 1
    else:
        return 0

def get_hash(plain_text):
    plain_text = plain_text.encode('utf-8')
    hash_object = hashlib.sha256(plain_text)
    hex_dig = hash_object.hexdigest()
    return hex_dig

def get_login(email, passwort):
    email = sql_escape(email)
    passwort = sql_escape(passwort)

    email = "'" + email + "'"
    init.dbcursor.execute("SELECT * FROM Benutzer WHERE email = " + email)
    result = init.dbcursor.fetchall()

    print(result)

    if check_hash(passwort, result[0][4]):
        session['id'] = str(result[0][0])
        session['email'] = str(result[0][3])
        session['hash'] = result[0][4]
        return 1
    else:
        return 0

def check_if_admin():
    id = "'" + session.get('id') + "'"
    try:
        init.dbcursor.execute("SELECT * FROM Benutzer WHERE Benutzer_ID=" + id)
    except Exception as e:
        print(e)
        abort(500)
    result = init.dbcursor.fetchall()
    if result[0][6] == 1:
        return 1
    else:
        return 0

def generate_navbar():
    navbar = (
        "<div id=\"Navbar\"> "
        "| <a href=\"/home\"> Home </a> |"
    )

    navbar = navbar + (
        "| <a href=\"/benutzer\"> Benutzer </a> |"
    )

    if check_if_admin():
        navbar = navbar + (
            "| <a href=\"/admin\"> Admin </a> |"
        )

    navbar = navbar + (
        "| <a href=\"/einkaufswagen\"> Einkaufswagen </a> |"
        "| <a href=\"/logout\"> Logout </a> |"
        "</div> <br>"
    )

    return navbar

def sql_escape(string):
    return string.replace("'", "''")

def geld_replace(string):
    string = re.sub('[^\d\.]', '', string)
    return string

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in init.ALLOWED_EXTENSIONS