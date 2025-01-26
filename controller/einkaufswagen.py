import models.einkaufswagen
import models.kaffee

def get_data_formated(id):
    einkaufswagen = models.einkaufswagen.get_all_by_user_id(id)
    result = []

    for data in einkaufswagen:
        kaffee_id = data[2]
        gramm = data[3]
        menge = data[4]

        kaffee = models.kaffee.get_by_id(kaffee_id) + (gramm, menge)

        result.append(kaffee)

    print(result)

    return result

def insert(kaffeeid, benutzerid, gramm, menge):
    data = models.einkaufswagen.get_by_kaffeeid_benutzerid_gramm(kaffeeid, benutzerid, gramm)

    if data:
        models.einkaufswagen.set_menge(data[0], int(data[3]) + int(menge))
    else:
        models.einkaufswagen.insert(benutzerid, kaffeeid, gramm, menge)

    return ""

def update(kaffeeid, benutzerid, gramm, menge):
    data = models.einkaufswagen.get_by_kaffeeid_benutzerid_gramm(kaffeeid, benutzerid, gramm)

    if data:
        models.einkaufswagen.set_menge(data[0], int(menge))

    return ""