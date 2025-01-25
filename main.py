from flask import Flask, render_template, request, redirect, session, abort
from datetime import datetime

import benutzer as b
import kaffee as k
import kaffeetemp as kt
import einkaufswagen as e
import functions
import init
from init import *

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return redirect('/login')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if session.get('id'):
            return redirect("/home")
        return render_template('login.html', html_lang=HTML_LANG, html_title=HTML_TITLE)
    elif request.method == 'POST':
        if session.get('id'):
            return redirect("/home")

        fehler = "Folgendes fehlt: "
        error = 0

        if request.form.get('email'):
            email = request.form['email']
        else:
            fehler = fehler + "email "
            error = 1

        if request.form.get('passwort'):
            passwort = request.form['passwort']
        else:
            fehler = fehler + "passwort "
            error = 1

        if error == 0:
            if functions.get_login(email, passwort):
                return redirect("/home")
            else:
                fehler = "E-Mail oder Passwort Falsch"
                return render_template('login.html', html_lang=HTML_LANG, html_title=HTML_TITLE, fehler=fehler)
        else:
            return render_template('login.html', html_lang=HTML_LANG, html_title=HTML_TITLE, fehler=fehler)

    else:
        return abort(404)

@app.route('/logout')
def logout():
    session.pop('id')
    fehler = "Ausgeloggt"
    return render_template('login.html', html_lang=HTML_LANG, html_title=HTML_TITLE, fehler=fehler)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        if session.get('id'):
            return render_template('home.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), result=k.get_all())
        else:
            return redirect("/login")
    elif request.method == 'POST':
        return redirect("/login")
    else:
        return redirect("/login")

@app.route('/benutzer', methods=['GET', 'POST'])
def benutzer():
    if session.get('id'):
        if request.method == 'GET':
            return render_template('benutzer/benutzer.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), benuter_daten=b.get_by_id(session.get('id')))

@app.route('/benutzer/aendern', methods=['GET', 'POST'])
def benutzer_aendern():
    if session.get('id'):
        if request.method == 'POST':
            fehler = ""
            vorname = ""
            nachname = ""
            email = ""
            adresse = ""
            passwort = ""

            if request.form.get('vorname'):
                vorname = request.form['vorname']
            if request.form.get('nachname'):
                nachname = request.form['nachname']
            if request.form.get('email'):
                email = request.form['email']
            if request.form.get('adresse'):
                adresse = request.form['adresse']
            if request.form.get('passwort') and request.form.get('passwort2'):
                if request.form.get('passwort') == request.form.get('passwort2'):
                    passwort = functions.get_hash(request.form.get('passwort'))
                else:
                    fehler = "Passwort nicht gleich"

            b.update(session.get('id'), vorname, nachname, email, passwort, adresse,str(b.get_by_id(session.get('id'))[4]))
            return render_template('benutzer/benutzer.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), benuter_daten=b.get_by_id(session.get('id')), fehler=fehler)
        return redirect("/benutzer")

@app.route('/einkaufswagen', methods=['GET', 'POST'])
def einkaufswagen():
    if session.get('id'):
        if request.method == 'GET':
            return render_template('einkaufswagen.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), result=e.get_all_user_id_formated(session.get('id')))
        elif request.method == 'POST':
            kaffee_id = request.form.get('id')
            gramm = request.form.get('gramm')
            menge = request.form.get('menge')

            if gramm=="0" or gramm == "":
                abort(404)

            benutzer_ID = session.get('id')

            e.insert(benutzer_ID, kaffee_id, menge, gramm)
            return "POST"
        else:
            abort(404)

@app.route('/einkaufswagen/set', methods=['GET', 'POST'])
def einkaufswagen_set():
    if session.get('id'):
        if request.method == 'POST':
            kaffee_id = request.form.get('id')
            gramm = request.form.get('gramm')
            menge = request.form.get('menge')

            if gramm == "0" or gramm == "":
                abort(404)

            benutzer_ID = session.get('id')

            e.update(benutzer_ID, kaffee_id, menge, gramm)
            return "POST"
    #abort(404)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if session.get('id'):
        if request.method == 'GET':
            return render_template('admin/admin.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar())

@app.route('/admin/delete')
def admin_delete():
    init.delete()
    return redirect("/install")
@app.route('/admin/fill')
def admin_fill():
    init.fill()
    return redirect("/admin")
@app.route('/admin/benutzer/fill')
def admin_benutzer_fill():
    b.fill()
    return redirect("/admin")
@app.route('/admin/kaffee/fill')
def admin_kaffee_fill():
    k.fill()
    return redirect("/admin")

@app.route('/admin/benutzer/hinzufuegen', methods=['GET', 'POST'])
def admin_benutzer_hinzufuegen():
    if session.get('id'):
        if functions.check_if_admin():
            if request.method == 'GET':
                    return render_template('admin/benutzer_hinzufuegen.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar())
            if request.method == 'POST':
                fehler = "Folgendes fehlt: "
                error = 0

                if request.form.get('vorname'):
                    vorname = request.form['vorname']
                else:
                    fehler = fehler + "vorname "
                    error = 1
                if request.form.get('nachname'):
                    nachname = request.form['nachname']
                else:
                    fehler = fehler + "nachname "
                    error = 1
                if request.form.get('email'):
                    email = request.form['email']
                else:
                    fehler = fehler + "email "
                    error = 1
                if request.form.get('adresse'):
                    adresse = request.form['adresse']
                else:
                    fehler = fehler + "adresse "
                    error = 1
                if request.form.get('admin'):
                    admin = request.form['admin']
                else:
                    fehler = fehler + "admin "
                    error = 1

                if request.form.get('passwort') and request.form.get('passwort2'):
                    if request.form.get('passwort') == request.form.get('passwort2'):
                        passwort = functions.get_hash(request.form.get('passwort'))
                    else:
                        fehler = "Passwort nicht gleich"
                else:
                    fehler = fehler + "passwort "
                    error = 1

                if error:
                    return render_template('admin/benutzer_hinzufuegen.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), fehler=fehler)
                else:
                    b.insert(vorname, nachname, email, passwort, adresse, admin)
                    fehler = "Benutzer hinzugefügt"
                    return render_template('admin/benutzer_hinzufuegen.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), fehler=fehler)

@app.route('/admin/benutzer/anzeigen', methods=['GET', 'POST'])
def admin_benutzer_anzeigen():
    if session.get('id'):
        if functions.check_if_admin():
            if request.method == 'GET':
                return render_template('admin/benutzer_anzeigen.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), result=b.get_all())

@app.route('/admin/benutzer/aendern/<id>', methods=['GET', 'POST'])
def admin_benutzer_aendern(id):
    if functions.check_if_admin():
        if request.method == 'GET':
            return render_template('admin/benutzer_aendern.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), result=b.get_by_id(id), id=id)
        if request.method == 'POST':
            error = 0
            fehler = ""
            vorname = ""
            nachname = ""
            email = ""
            adresse = ""
            passwort = ""
            admin = ""
            if request.form.get('vorname'):
                vorname = request.form['vorname']
            if request.form.get('nachname'):
                nachname = request.form['nachname']
            if request.form.get('email'):
                email = request.form['email']
            if not email:
                error = 1
                fehler = "E-Mail Fehlt"
            if request.form.get('adresse'):
                adresse = request.form['adresse']
            if request.form.get('admin'):
                admin = request.form['admin']
            if request.form.get('passwort') and request.form.get('passwort2'):
                if request.form.get('passwort') == request.form.get('passwort2'):
                    passwort = functions.get_hash(request.form.get('passwort'))
                else:
                    fehler = "Passwort nicht gleich"


            if error:
                return render_template('admin/benutzer_aendern.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), result=b.get_by_id(id), id=id, fehler=fehler)
            else:
                b.update(id, vorname, nachname, email, passwort, adresse, admin, )

                return redirect("/admin/benutzer/anzeigen")

@app.route('/admin/benutzer/loeschen/<id>', methods=['GET', 'POST'])
def admin_benutzer_loeschen(id):
    b.loeschen(id)
    return redirect('/admin/benutzer/anzeigen')
@app.route('/admin/kaffee/hinzufuegen', methods=['GET', 'POST'])
def admin_kaffee_hinzufuegen():
    if session.get('id'):
        if functions.check_if_admin():
            if request.method == 'GET':
                return render_template('admin/kaffee_hinzufuegen.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar())
            if request.method == 'POST':
                fehler = "Folgendes fehlt: "
                error = 0
                leer = 0

                hersteller = ""
                herkunft = ""
                name=""
                anbauart = ""
                besonderheit = ""
                geschmacksprofil = ""
                preis_1000g = ""
                preis_500g = ""
                preis_250g = ""
                preis_100g = ""

                if request.form.get('hersteller'):
                    hersteller = request.form['hersteller']
                else:
                    fehler = fehler + "hersteller "
                    error = 1

                if request.form.get('name'):
                    name = request.form['name']
                else:
                    fehler = fehler + "name "
                    error = 1

                if request.form.get('herkunft'):
                    herkunft = request.form['herkunft']

                if request.form.get('anbauart'):
                    anbauart = request.form['anbauart']

                if request.form.get('besonderheit'):
                    besonderheit = request.form['besonderheit']

                if request.form.get('geschmacksprofil'):
                    geschmacksprofil = request.form['geschmacksprofil']


                if request.form.get('preis_1000g'):
                    preis_1000g = request.form['preis_1000g']
                    preis_1000g.replace(" ", "")
                if not preis_1000g:
                    leer = leer + 1

                if request.form.get('preis_500g'):
                    preis_500g = request.form['preis_500g']
                    preis_500g.replace(" ", "")
                if not preis_500g:
                    leer = leer + 1

                if request.form.get('preis_250g'):
                    preis_250g = request.form['preis_250g']
                    preis_250g.replace(" ", "")
                if not preis_250g:
                    leer = leer + 1

                if request.form.get('preis_100g'):
                    preis_100g = request.form['preis_100g']
                    preis_100g.replace(" ", "")
                if not preis_100g:
                    leer = leer + 1

                if leer == 4:
                    error = 1
                    fehler = "Preis Leer"

                if error:
                    return render_template('admin/kaffee_hinzufuegen.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), fehler=fehler)
                else:
                    k.insert(hersteller, name, herkunft, anbauart, besonderheit, geschmacksprofil, preis_1000g, preis_500g, preis_250g, preis_100g)
                    fehler = "Kaffee hinzugefügt"
                    return render_template('admin/kaffee_hinzufuegen.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), fehler=fehler)

@app.route('/admin/kaffee/anzeigen', methods=['GET', 'POST'])
def admin_kaffee_anzeigen():
    if session.get('id'):
        if functions.check_if_admin():
            if request.method == 'GET':
                return render_template('admin/kaffee_anzeigen.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), result=k.get_all())

@app.route('/admin/kaffee/aendern/<id>', methods=['GET', 'POST'])
def admin_kaffee_aendern(id):
    if functions.check_if_admin():
        if request.method == 'GET':
            return render_template('admin/kaffee_aendern.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), result=k.get_by_id(id),id=id)
        if request.method == 'POST':
            fehler = "Folgendes fehlt: "
            error = 0
            leer = 0

            hersteller = ""
            herkunft = ""
            name = ""
            anbauart = ""
            besonderheit = ""
            geschmacksprofil = ""
            preis_1000g = ""
            preis_500g = ""
            preis_250g = ""
            preis_100g = ""

            if request.form.get('hersteller'):
                hersteller = request.form['hersteller']
            else:
                fehler = fehler + "hersteller "
                error = 1

            if request.form.get('name'):
                name = request.form['name']
            else:
                fehler = fehler + "name "
                error = 1

            if request.form.get('herkunft'):
                herkunft = request.form['herkunft']

            if request.form.get('anbauart'):
                anbauart = request.form['anbauart']

            if request.form.get('besonderheit'):
                besonderheit = request.form['besonderheit']

            if request.form.get('geschmacksprofil'):
                geschmacksprofil = request.form['geschmacksprofil']

            if request.form.get('preis_1000g'):
                preis_1000g = request.form['preis_1000g']
                preis_1000g.replace(" ", "")
                preis_1000g.replace(",", ".")
            if not preis_1000g:
                leer = leer + 1
                preis_1000g = ""

            if request.form.get('preis_500g'):
                preis_500g = request.form['preis_500g']
                preis_500g.replace(" ", "")
                preis_500g.replace(",", ".")
            if not preis_500g:
                leer = leer + 1
                preis_500g = ""

            if request.form.get('preis_250g'):
                preis_250g = request.form['preis_250g']
                preis_250g.replace(" ", "")
                preis_250g.replace(",", ".")
            if not preis_250g:
                leer = leer + 1
                preis_250g = ""

            if request.form.get('preis_100g'):
                preis_100g = request.form['preis_100g']
                preis_100g.replace(" ", "")
                preis_100g.replace(",", ".")
            if not preis_100g:
                leer = leer + 1
                preis_100g = ""

            if leer == 4:
                error = 1
                fehler = "Preis Leer"

            if error:
                return render_template('admin/kaffee_aendern.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), result=k.get_by_id(id),id=id, fehler=fehler)
            else:
                k.update(id, hersteller, name, herkunft, anbauart, besonderheit, geschmacksprofil, preis_1000g, preis_500g, preis_250g, preis_100g)
                fehler = "Kaffee hinzugefügt"
                return redirect('/admin/kaffee/anzeigen')

@app.route('/admin/kaffee/loeschen/<id>', methods=['GET', 'POST'])
def admin_kaffee_loeschen(id):
    k.loeschen(id)
    return redirect('/admin/kaffee/anzeigen')

@app.route('/install', methods=['POST', 'GET'])
def install():
    if request.method == 'GET':
        try:
            init.dbcursor.execute("SELECT * FROM Benutzer")
            return redirect("/login")
        except Exception as e:
            return render_template('admin/install.html', html_lang=HTML_LANG, html_title=HTML_TITLE)
    elif request.method == 'POST':
        fehler = "Folgendes fehlt: "
        error = 0

        if request.form.get('vorname'):
            vorname = request.form['vorname']
        else:
            fehler = fehler + "vorname "
            error = 1

        if request.form.get('nachname'):
            nachname = request.form['nachname']
        else:
            fehler = fehler + "nachname "
            error = 1

        if request.form.get('email'):
            email = request.form['email']
        else:
            fehler = fehler + "email "
            error = 1

        if request.form.get('passwort'):
            passwort = request.form['passwort']
        else:
            fehler = fehler + "passwort "
            error = 1

        if request.form.get('adresse'):
            adresse = request.form['adresse']
        else:
            fehler = fehler + "adresse "
            error = 1

        admin = "1"

        if error == 0:
            init.install()
            b.insert(vorname, nachname, email, passwort, adresse, admin)
            return redirect("/login")
        else:
            return render_template('admin/install.html', html_lang=HTML_LANG, html_title=HTML_TITLE, fehler=fehler)
    else:
        return abort(404)

@app.route('/fill')
def fill():
    init.fill()
    return "fill"

@app.route('/delete')
def delete():
    init.delete()
    return "delete"

@app.route('/admin/einkaufswagen/delete')
def admin_einkaufswagen_delete():
    init.delete_einkaufswagen()
    return redirect("/admin")

@app.route('/admin/kaffee/delete')
def admin_kaffee_delete():
    init.delete_kaffee()
    return redirect('/admin/kaffee/anzeigen')

@app.route('/admin/kaffee/import/txt', methods=['POST', 'GET'])
def admin_kaffee_import_txt():
    if request.method == 'GET':
        return render_template('admin/admin_import.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar())
    if request.method == 'POST':
        data = request.form.get('importtext')
    try:
        data = data.split("\r\n")
        for row in data:
            row = row.split(";")

            hersteller = row[0] or ""
            name = row[1] or ""
            herkunft = row[2] or ""
            anbauart = row[3] or ""
            besonderheit = row[4] or ""
            geschmacksprofil = row[5] or ""
            preis_1000g = row[6] or ""
            preis_500g = row[7] or ""
            preis_250g = row[8] or ""
            preis_100g = row[9] or ""

            k.insert(hersteller, name, herkunft, anbauart, besonderheit, geschmacksprofil, preis_1000g, preis_500g, preis_250g, preis_100g)
    except Exception as e:
        print(e)
    fehler = "importiert"
    return render_template('admin/admin_import.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), fehler=fehler)

@app.route('/admin/kaffee/import/file', methods=['POST', 'GET'])
def admin_kaffee_import_file():
    if request.method == 'GET':
        return render_template('admin/admin_import_file.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar())
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file and functions.allowed_file(file.filename):
            now = datetime.now()
            dt_string = now.strftime("%d%m%Y-%H%M%S")

            filename = dt_string + "-" + file.filename

            save = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(save)

            with open(save) as file:
                for line in file:
                    data = line.rstrip()
                    data = data.split(';')

                    hersteller = data[0] or ""
                    name = data[1] or ""
                    herkunft = data[2] or ""
                    anbauart = data[3] or ""
                    besonderheit = data[4] or ""
                    geschmacksprofil = data[5] or ""
                    preis_1000g = data[6] or ""
                    preis_500g = data[7] or ""
                    preis_250g = data[8] or ""
                    preis_100g = data[9] or ""

                    kt.insert(hersteller, name, herkunft, anbauart, besonderheit, geschmacksprofil, preis_1000g, preis_500g, preis_250g, preis_100g)

            return render_template('admin/import_file_check.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), result=kt.get_all(), filename=save)

        return redirect("/admin/kaffee/import/file")

@app.route('/admin/kaffee/import/file/test', methods=['POST', 'GET'])
def admin_kaffee_import_file_test():
    if request.method == 'POST':

        try:
            dbcursor.execute("DELETE FROM Kaffeetemp")
        except Exception as e:
            print(e)
            print("Could not delete Table Benutzer")

        if request.form.get('file'):
            with open(request.form.get('file')) as file:
                for line in file:
                    data = line.rstrip()
                    data = data.split(';')

                    hersteller = data[0] or ""
                    name = data[1] or ""
                    herkunft = data[2] or ""
                    anbauart = data[3] or ""
                    besonderheit = data[4] or ""
                    geschmacksprofil = data[5] or ""
                    preis_1000g = data[6] or ""
                    preis_500g = data[7] or ""
                    preis_250g = data[8] or ""
                    preis_100g = data[9] or ""

                    k.insert(hersteller, name, herkunft, anbauart, besonderheit, geschmacksprofil, preis_1000g, preis_500g, preis_250g, preis_100g)

            return redirect("/admin/kaffee/anzeigen")

        else:
            return redirect("/admin/kaffee/import/file")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
