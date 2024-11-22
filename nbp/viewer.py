from flask import Flask, redirect, render_template
from sqlalchemy import text
from utils.config import load_config
from utils.db import disconnect_from_db, open_db

# CONFIG_FILE = "db_config.yaml"
CONFIG_FILE = "db_config_lukasz.yaml"

app = Flask("nasza apka")

config = load_config(CONFIG_FILE)


def lista_walut():
    db_conn = open_db(config)
    res = db_conn.execute(text("select distinct waluta from waluty order by waluta"))
    res = list(res)
    disconnect_from_db(db_conn)
    return res


def notowania_waluty(waluta, data_od, data_do):
    db_conn = open_db(config)
    query = f"""select data, kurs
                from waluty
                where data >= '{data_od}'
                and data <= '{data_do}'
                and waluta = '{waluta}'
            """
    res = db_conn.execute(text(query))
    columns = list(res.keys())
    wynik = [{columns[0]: r[0], columns[1]: r[1]} for r in res]
    disconnect_from_db(db_conn)
    return wynik


@app.route("/")
def strona_glowna():
    return redirect("/kurs/EUR/2024-11-01/2024-11-30")


@app.route("/kurs/<waluta>/<data_od>/<data_do>")
def kurs(waluta, data_od, data_do):
    # dost_wal = [{"waluta": "EUR"}, {"waluta": "USD"}, {"waluta": "byle co"}]
    dost_wal = lista_walut()
    # kwotowania = [
    #     {"data": "data1", "kurs": 123},
    #     {"data": "data2", "kurs": 456},
    #     {"data": "data3", "kurs": 789},
    # ]
    kwotowania = notowania_waluty(waluta, data_od, data_do)

    return render_template(
        "nbp.html", dostepne_waluty=dost_wal, kursy=kwotowania, curr_wal=waluta
    )


if __name__ == "__main__":
    app.run(debug=True)
