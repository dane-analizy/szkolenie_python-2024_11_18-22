# moduły = zbiory funkcji w oddzielnym pliku
# zobacz plik "narzedzia.py"

# from narzedzia import bmi
# from narzedzia import as_float

# wynik = bmi(80, 180)
# print(wynik)

# print(as_float("124.515"))


# uwaga - kod w importowanych rzeczach się wykonuje
# import modul_test

# modul_test.hello("Łukasz")
# print(modul_test.zmienna_x)


# __name__

# print(__name__)  # __main__

# import modul_dwa # <- cały plik modul_dwa.py się wykona

# if __name__ == "__main__":
#     print("uruchomiłeś mnie (jestem main.py)")


# tradycyjna struktura kodu:

# import time
# import json

# import yaml

# from narzedzia import bmi

# STALA = 12345

# def funkcja():
#     """Nic nie robi, bo to przykład"""
#     pass

# def main():
#     # tutaj główny kod programu
#     pass

# if __name__ == '__main__':
#     main()


# pakiety

# import utils.etl

# print(utils.etl.as_float("124"))


##### ZADANIE bez numeru

# Przenieś funkcje z poprzednich zadań (czytającą dane z pliku oraz wyświetlającą listę)
# do oddzielnego modułu `utils`. Użyj ich po zaimportowaniu z plików.

# from utils.operations import wczytaj_czyste_dane
# from utils.calc import bmi

# dane = wczytaj_czyste_dane("osoby.csv")

# for o in dane:
#     print(f"{o['imie']}: BMI = {bmi(o['waga'], o['wzrost'])}")


# Współpraca z usługami sieciowymi

# https://httpbin.org/
# https://it-tools.tech/

# pakiet requests
# pip install requests
# import requests

# get - pobierz
# response = requests.get("https://onet.pl")

# print(response.status_code)
# if response.status_code == 200:
#     print("Udało się otrzymać odpowiedź z serwera")

# print(response.content)


# GET do API NBP

# import requests
# url = "https://api.nbp.pl/api/exchangerates/tables/A/2024-11-21?format=json"
# res = requests.get(url)
# print(res.content)
# print(res.text)
# dane = res.json()
# print(dane)
# print(type(dane))

# print(dane[0])
# print(type(dane[0]))


# notowanie z jednego dnia
# import requests


# rok = 2024
# miesiac = 11
# dzien = 21

# url = f"https://api.nbp.pl/api/exchangerates/tables/A/{rok}-{miesiac}-{dzien}?format=json"

# res = requests.get(url)
# if res.status_code != 200:
#     print(f"Błąd: {res.status_code}")

# dane = res.json()
# notowanie = dane[0]
# kursy = notowanie["rates"]

# for waluta in kursy:
#     print(waluta)


# zobacz   filter(lambda k: k.get("code").lower() in obslugiwane_waluty, kursy)


#### ZADANIE 33

# Pobierz dane z NBP i wyświetl na konsoli kurs:
# franka (chf), euro (eur) i dolara (usd) oraz pole effectiveDate
# dla wszystkich dni z listopada 2024 (1-30)
# Brak notowania z danego dnia rozpoznasz po status code != 200


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
        if waluta.get("code").lower() in obslugiwane_waluty:
            wynik[waluta.get("code")] = waluta.get("mid")

    return wynik


for d in range(1, 31):
    sitko_walut = get_nbp_data(dzien=d, obslugiwane_waluty=["jpy", "idr"])
    print(sitko_walut)
    sitko_walut = get_nbp_data(dzien=d, obslugiwane_waluty=["jpy", "idr"])
    print(sitko_walut)
