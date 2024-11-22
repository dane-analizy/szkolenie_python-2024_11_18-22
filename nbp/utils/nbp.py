from datetime import datetime

import requests


def get_nbp_data(
    rok=None,
    miesiac=None,
    dzien=None,
    obslugiwane_waluty=["eur", "chf", "usd"],
):
    teraz = datetime.now()
    if not rok:
        rok = teraz.year
    if not miesiac:
        miesiac = teraz.month
    if not dzien:
        dzien = teraz.day

    wynik = {"data": f"{rok}-{miesiac:02}-{dzien:02}"}

    url = f"https://api.nbp.pl/api/exchangerates/tables/A/{rok}-{miesiac:02}-{dzien:02}?format=json"
    res = requests.get(url)
    if res.status_code != 200:
        return wynik

    dane = res.json()
    notowanie = dane[0]
    kursy = notowanie["rates"]

    for waluta in kursy:
        if waluta.get("code").upper() in obslugiwane_waluty:
            wynik[waluta.get("code")] = waluta.get("mid")

    return wynik
