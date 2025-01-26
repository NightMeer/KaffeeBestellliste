from flask import Flask, render_template, request, redirect, session, abort
from datetime import datetime

import controller.benutzer
import controller.kaffee
import controller.einkaufswagen
import controller.kaffeetemp
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
    if not session.get('id'):
        if request.method == 'GET':
            return render_template("login.html", html_lang=HTML_LANG, html_title=HTML_TITLE)
        else:
            if not functions.get_login(request.form.get('email'), request.form.get('passwort')):
                return render_template('login.html', html_lang=HTML_LANG, html_title=HTML_TITLE)
    return redirect("/home")

@app.route('/logout')
def logout():
    session.pop('id')
    session.pop('email')
    session.pop('hash')
    return render_template('login.html', html_lang=HTML_LANG, html_title=HTML_TITLE)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if session.get('id'):
        if request.method == 'GET':
            return render_template('home.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), result=controller.kaffee.get_all())
        else:
            controller.einkaufswagen.insert(kaffeeid=request.form.get('kaffeeid'), benutzerid=session.get('id'), gramm=request.form.get('gramm'), menge=request.form.get('menge'))
            return "1"
    return redirect("/login")

@app.route('/benutzer', methods=['GET'])
def benutzer():
    if session.get('id'):
        return render_template('benutzer/benutzer.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), benuter_daten=controller.benutzer.get_by_id(session.get('id')))
    else:
        return redirect("/login")

# Benutzer aendern
@app.route('/benutzer/aendern', methods=['POST'])
def benutzer_aendern():
    if session.get('id'):
        passwort = functions.check_passwort(request.form.get('passwort'), request.form.get('passwort2'))
        if passwort:
            controller.benutzer.update(id=session.get('id'), passwort=passwort)

        controller.benutzer.update(id=session.get('id'), vorname=request.form.get('vorname'), nachname=request.form.get('nachname'), email=request.form.get('email'), adresse=request.form.get('adresse'))

        return render_template('benutzer/benutzer.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), benuter_daten=controller.benutzer.get_by_id(session.get('id')))

    return redirect("/login")

@app.route('/einkaufswagen', methods=['GET', 'POST'])
def einkaufswagen():
    if session.get('id'):
        if request.method == 'GET':
            return render_template('einkaufswagen.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), result=controller.einkaufswagen.get_data_formated(session.get('id')))
        else:
            controller.einkaufswagen.update(kaffeeid=request.form.get('kaffeeid'), benutzerid=session.get('id'), gramm=request.form.get('gramm'), menge=request.form.get('menge'))
            return "1"
    return redirect("/login")

# Admin
@app.route('/admin', methods=['GET'])
def admin():
    if session.get('id'):
            return render_template('admin/admin.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar())

# Benutzer hinzufügen
@app.route('/admin/benutzer/hinzufuegen', methods=['GET', 'POST'])
def admin_benutzer_hinzufuegen():
    if functions.check_if_admin():
        if request.method == 'GET':
                return render_template('admin/benutzer_hinzufuegen.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar())
        if request.method == 'POST':
            passwort = functions.check_passwort(request.form.get('passwort'), request.form.get('passwort2'))

            if passwort:
                controller.benutzer.insert(vorname=request.form.get('vorname'), nachname=request.form.get('nachname'), email=request.form.get('email'), passwort=passwort, adresse=request.form.get('adresse'), admin=request.form.get('admin'))
            else:
                return render_template('admin/benutzer_hinzufuegen.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar())
            return redirect('/admin/benutzer/anzeigen')
    else:
        return redirect('/login')

@app.route('/admin/benutzer/anzeigen', methods=['GET'])
def admin_benutzer_anzeigen():
    if functions.check_if_admin():
        return render_template('admin/benutzer_anzeigen.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), result=controller.benutzer.get_all())
    else:
        return redirect('/login')

@app.route('/admin/benutzer/aendern/<id>', methods=['GET', 'POST'])
def admin_benutzer_aendern(id):
    if functions.check_if_admin():
        if request.method == 'GET':
            return render_template('admin/benutzer_aendern.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), benuter_daten=controller.benutzer.get_by_id(id), id=id)
        if request.method == 'POST':
            passwort = functions.check_passwort(request.form.get('passwort'), request.form.get('passwort2'))
            if passwort:
                controller.benutzer.update(id=id, passwort=passwort)

            controller.benutzer.update(id=id, vorname=request.form.get('vorname'), nachname=request.form.get('nachname'), email=request.form.get('email'), adresse=request.form.get('adresse'))

            return render_template('admin/benutzer_aendern.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), id=id, benuter_daten=controller.benutzer.get_by_id(id))
    else:
        return redirect('/login')

# Benutzuer löschen
@app.route('/admin/benutzer/loeschen/<id>', methods=['POST'])
def admin_benutzer_loeschen(id):
    if functions.check_if_admin():
        controller.benutzer.delete_by_id(id)
        return redirect('/admin/benutzer/anzeigen')
    else:
        return redirect('/login')

@app.route('/admin/kaffee/hinzufuegen', methods=['GET', 'POST'])
def admin_kaffee_hinzufuegen():
    if functions.check_if_admin():
        if request.method == 'GET':
            return render_template('admin/kaffee_hinzufuegen.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar())
        if request.method == 'POST':

            controller.kaffee.insert(hersteller=request.form.get('hersteller'), name=request.form.get('name'), herkunft=request.form.get('herkunft'), anbauart=request.form.get('anbauart'), besonderheit=request.form.get('besonderheit'), geschmacksprofil=request.form.get('geschmacksprofil'), preis_1000g=request.form.get('preis_1000g'), preis_500g=request.form.get('preis_500g'), preis_250g=request.form.get('preis_250g'), preis_100g=request.form.get('preis_100g'))
            return render_template('admin/kaffee_hinzufuegen.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar())
    else:
        return redirect('/login')

# Kaffee Anzeigen
@app.route('/admin/kaffee/anzeigen', methods=['GET'])
def admin_kaffee_anzeigen():
    if functions.check_if_admin():
        return render_template('admin/kaffee_anzeigen.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), result=controller.kaffee.get_all())
    else:
        return redirect('/login')

# Kaffee Ändern
@app.route('/admin/kaffee/aendern/<id>', methods=['GET', 'POST'])
def admin_kaffee_aendern(id):
    if functions.check_if_admin():
        if request.method == 'GET':
            return render_template('admin/kaffee_aendern.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), result=controller.kaffee.get_by_id(id),id=id)
        if request.method == 'POST':
            controller.kaffee.update(id=id, hersteller=request.form.get('hersteller'), name=request.form.get('name'), herkunft=request.form.get('herkunft'), anbauart=request.form.get('anbauart'), besonderheit=request.form.get('besonderheit'), geschmacksprofil=request.form.get('geschmacksprofil'), preis_1000g=request.form.get('preis_1000g'), preis_500g=request.form.get('preis_500g'), preis_250g=request.form.get('preis_250g'), preis_100g=request.form.get('preis_100g'))
            return redirect('/admin/kaffee/anzeigen')
    else:
        return redirect('/login')

# Kaffee Löschen
@app.route('/admin/kaffee/loeschen/<id>', methods=['GET', 'POST'])
def admin_kaffee_loeschen(id):
    controller.kaffee.loeschen(id)
    return redirect('/admin/kaffee/anzeigen')

# Install
@app.route('/install', methods=['POST', 'GET'])
def install():
    if request.method == 'GET':
        if controller.benutzer.dbexist():
            return redirect("/login")
        else:
            return render_template('admin/install.html', html_lang=HTML_LANG, html_title=HTML_TITLE)
    else:
        init.install()
        controller.benutzer.insert(vorname=request.form.get('vorname'), nachname=request.form.get('nachname'), email=request.form.get('email'), passwort=request.form.get('passwort'), adresse=request.form.get('adresse'), admin="1")
        return redirect("/login")

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

            controller.kaffee.insert(hersteller, name, herkunft, anbauart, besonderheit, geschmacksprofil, preis_1000g, preis_500g, preis_250g, preis_100g)
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
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
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

                    controller.kaffeetemp.insert(hersteller, name, herkunft, anbauart, besonderheit, geschmacksprofil, preis_1000g, preis_500g, preis_250g, preis_100g)

            return render_template('admin/import_file_check.html', html_lang=HTML_LANG, html_title=HTML_TITLE, navbar=functions.generate_navbar(), result=controller.kaffeetemp.get_all(), filename=save)

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

                    controller.kaffee.insert(hersteller, name, herkunft, anbauart, besonderheit, geschmacksprofil, preis_1000g, preis_500g, preis_250g, preis_100g)

            return redirect("/admin/kaffee/anzeigen")

        else:
            return redirect("/admin/kaffee/import/file")

# Prod Löschen:
@app.route('/fill')
def fill():
    init.fill()
    return "fill"
@app.route('/delete')
def delete():
    init.delete()
    return "delete"
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
    controller.benutzerfill()
    return redirect("/admin")
@app.route('/admin/kaffee/fill')
def admin_kaffee_fill():
    controller.kaffee.fill()
    return redirect("/admin")
@app.route('/admin/einkaufswagen/delete')
def admin_einkaufswagen_delete():
    init.delete_einkaufswagen()
    return redirect("/admin")
@app.route('/admin/kaffee/delete')
def admin_kaffee_delete():
    init.delete_kaffee()
    return redirect('/admin/kaffee/anzeigen')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

