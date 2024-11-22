# jsony -> przykład w pliku dane.json

# wczytanie jsona
# import json

# with open("dane.json", "r", encoding="utf-8") as fp:
#     dane = json.load(fp)

# print(dane)
# print(type(dane))

# print()

# for k,v in dane.items():
#     print(k,v)

# print()

# for el in dane.get("users"):
#     print(el)


# zapisanie
# import json

# d = {
#     "Tom": {"waga": 68, "wzrost": 170},
#     "Lady": {"waga": 68, "wzrost": 170},
# }

# with open("dane_2.json", "w", encoding="utf-8") as fp:
#     json.dump(d, fp)
#     s = json.dumps(d)

# print(s)
# print(d)


#### ZADANIE 28

# Korzystając z pakietu Faker przygotuj 5 rekordów składających się z: imienia, nazwiska,
# numeru telefonu osoby.
# Rekordy umieść na liście, a następnie zapisz każdy z nich (iterując po liście) w pliku JSON,
# którego nazwa to kolejny numer (1.json, 2.json)


# import json

# from faker import Faker

# fake = Faker(locale="pl")

# lista = []
# for i in range(5):
#     lista.append(
#         {
#             "imię": fake.first_name(),
#             "nazwisko": fake.last_name(),
#             "telefon": fake.phone_number(),
#         }
#     )

# lista = [
#     {
#         "imie": fake.first_name(),
#         "nazwisko": fake.last_name(),
#         "telefon": fake.phone_number(),
#     }
#     for _ in range(5)
# ]

# for i, o in enumerate(lista, start=1):
#     with open(f"{i}.json", "w", encoding="utf-8") as fp:
#         json.dump(o, fp)

# str(i) + ".json"
# f"{i}.json"


# pandas z listy słowników robi dataframe na pstryknięcie:
# import pandas as pd
# lista = [
#     {"productId": 1, "productName": "Laptop", "quantity": 1, "price": 1999.99},
#     {"productId": 2, "productName": "Monitor", "quantity": 1, "price": 399.99},
# ]
# df = pd.DataFrame(lista)
# print(df)


# import json

# from faker import Faker

# fake = Faker(locale="pl")

# lista_osob = []
# for i in range(5):
#     f_name = fake.first_name()
#     l_name = fake.last_name()
#     number = fake.phone_number()
#     slownik_jedna_osoba = {"imie": f_name, "nazwisko": l_name, "telefon": number}
#     lista_osob.append(slownik_jedna_osoba)


# for numer_obiektu, obiekt in enumerate(lista_osob, start=1):
#     nazwa_pliku = f"{numer_obiektu}_dane_lukasza.json"
#     with open(nazwa_pliku, "w", encoding="UTF-8") as plik:
#         json.dump(obiekt, plik)


# yamle

# czytanie z pliku YAML
# potrzebny pakiet PyYAML
# pip install PyYAML

# wczytanie YAMLa
# import yaml

# with open("dane.yaml", "r", encoding="utf-8") as fp:
#     dane = yaml.safe_load(fp) ## UWAGA - nie .load()

# print(dane)
# print(type(dane))


# zapisanie YAMLa
# import yaml
# import json

# # wczytanie jsona
# with open("dane.json", "r", encoding="utf-8") as fp:
#     dane = json.load(fp)

# # zapisanie tych samych danych do yamla
# with open("dane_zapisane.yaml", "w", encoding="utf-8") as fp:
#     yaml.dump(dane, fp, sort_keys=False)


### konfiguracja w pliku
# plik -> config.yaml

### ZADANIE 29

# Wczytaj z pliku 'config.yaml' konfigurację dostępu do bazy danych,
# niech będzie zapisana w zmiennej 'config'

# import yaml

# with open("config.yaml", "r", encoding="utf-8") as fp:
#     config = yaml.safe_load(fp)

# print(config)
# print(config['db_user'])


### funkcje + moduły


# def funkcja():
#     print("jestem w funkcji")
#     print("nadal jestem w funkcji")

#     for i in range(5):
#         print(i)

#     print("nadal jestem w funkcji, ale już kończę")


# def funkcja_dwa():
#     print("jestem funkcja 2")


# print("poza funkcją - przed wywołaniem")
# funkcja()
# print("po wykonananiu funkcji pierwszy raz")
# funkcja_dwa()
# funkcja()
# funkcja_dwa()
# print("po wykonananiu wszystkich funkcji")


# argumenty
# def funkcja_z_argumentem(liczba, napis):
#     # sprawdzenie typu argumentu 'liczba'
#     # if isinstance(liczba, (int, float) ):
#     #     print(f"Argument {liczba=}")
#     # else:
#     #     print(f"Podaj liczbę a nie {type(liczba)}")
#     print(f"Argument {liczba=}")
#     print(f"Argument {napis=}")


# # funkcja_z_argumentem(123, "ala ma kota")
# # funkcja_z_argumentem(99.99, "żyrafy wchodzą na szafy")

# # funkcja nie sprawdzi czy podane argumenty są odpowiednich typów
# # funkcja_z_argumentem("ala ma kota", [1, 2, 3])

# c = 1000
# d = 0
# # zwracanie czegoś z funkcji
# def dodaj(a, b):
#     d = 10_000
#     suma = a + b + c + d
#     print("Suma w środku funkcji:", suma)
#     return suma


# print(c)
# print(dodaj(10, 5))
# print(d)
# print(dodaj(20, 19))

# print(a, b)
# print(suma)


# def czy_dodatnia(a):
#     if a > 0:
#         return "dodatnie"
#     elif a <0:
#         return "ujemne"
#     else:
#         return "zero"


# def czy_dodatnia(a):
#     znak = "zero"
#     if a > 0:
#         znak = "dodatnie"
#     elif a < 0:
#         znak = "ujemne"

#     return znak

#### ZADANIE 30

# Przygotuj funkcję bmi(), która wyliczy na podstawie wagi i wzrostu (parametry) BMI z dokładnością
# do 2 miejsc po przecinku.
# W przypadku pojawienia się wyjątku (try..except) - wypisze na konsoli błąd i zwróci wartość -1

# bmi = weight / (height**2)


# rozwiązanie zadania oraz dokumentowanie funkcji
# def bmi(masa: float, wzrost: float) -> float:
#     """Funkcja oblicza wskaźnik BMI.

#     Argumenty:
#      - masa = waga w kg
#      - wzrost = wysokość w cm lub m (o ile mniej niż 3 m)

#     Zwraca:
#      - wartość współczynnika BMI albo -1 jeśli błąd
#     """
#     try:
#         if wzrost > 3:
#             wzrost = wzrost / 100
#         bmi = masa / wzrost**2
#         return bmi
#     except Exception as error:
#         print("Błąd:", error)
#         return -1


# print(bmi(80, "180"))
# print(bmi(80, 180))


# napis = "ala ma kota\na bożena ma psa"
# print(napis)

# def guwhguwg():
#     napis_wielolinijkowy = """pierwsza

#         druga (a właściwie 3)
# czwarta
# (puste)"""
#     print(napis_wielolinijkowy)

# guwhguwg()


# argumenty nazwane i argumenty domyślne


# def funkcja(a, b, c):
#     print(f"""
#           {a=}
#           {b=}
#           {c=}
#     """)


# # funkcja(1213, "napisa", 3)
# funkcja(c=3, a=5, b=1)
# funkcja(123, c=567, b=987)

# # funkcja(12300, c=56700, 98700)


# def funkcja(a, b=500, c=100):
#     print(f"""
#           {a=}
#           {b=}
#           {c=}
#     """)

# # funkcja(1, 2)
# # funkcja(1, c=2)
# # funkcja(1, b=2)
# funkcja(a=25)
# funkcja(75)


### ZADANIE 31

# Napisz funkcję która zwróci pod postacią listy list zawartość pliku,
# którego nazwę przekażemy przez pierwszy argument funkcji.
# Plik ma być otwarty z kodowaniem podanym jako drugi argument funkcji.
# Jeśli kodowanie nie zostanie podane ma przyjąć utf-8.


# def czytaj_plik(nazwa_pliku, separator=";", kodowanie="utf-8"):
#     dane = []
#     try:
#         with open(nazwa_pliku, "r", encoding=kodowanie) as f:
#             dane = [tuple(linia.strip().split(separator)) for linia in f]
#     except Exception as e:
#         print(e)
#     return dane

# dane_z_pliku = czytaj_plik("osoby.csv")
# print(dane_z_pliku)


### ZADANIE 32

# Napisz funkcję, która korzystając z danych (i funkcji) z poprzedniego zadania "oczyści" wczytanie
# informacje - czyli zmieni typy dla wzrostu i wagi.
# Dla chętnych: niech wynikiem będzie lista słowników o odpowiednich kluczach
# (imie, nazwisko, wzrost, waga).


# w ramach rozwiązania używamy wcześniejszej funkcji:
def czytaj_plik(nazwa_pliku, separator=";", kodowanie="utf-8"):
    dane = []
    try:
        with open(nazwa_pliku, "r", encoding=kodowanie) as f:
            dane = [tuple(linia.strip().split(separator)) for linia in f]
    except Exception as e:
        print(e)
    return dane


def as_float(s):
    try:
        f = float(s)
        return f
    except Exception as e:
        print(e)
        return None


def oczysc_dane(dane):
    oczyszczone_dane = []
    for i in dane:
        oczyszczone_dane.append(
            {
                "imie": i[0],
                "nazwisko": i[1],
                "wzrost": as_float(i[2]),
                "waga": as_float(i[3]),
            }
        )
    return oczyszczone_dane


def wczytaj_czyste_dane(nazwa_pliku, separator=";", kodowanie="utf-8"):
    dane_z_pliku = czytaj_plik(nazwa_pliku, separator=separator, kodowanie=kodowanie)
    dane_czyste = oczysc_dane(dane_z_pliku)
    return dane_czyste


dane_czyste_z_pliku = wczytaj_czyste_dane("osoby.csv")
# print(dane_czyste_z_pliku)


# dodajmy wyliczenie BMI na oczyszczonych danych
def bmi(masa: float, wzrost: float) -> float:
    try:
        if wzrost > 3:
            wzrost = wzrost / 100
        bmi = masa / wzrost**2
        return bmi
    except Exception as error:
        print("Błąd:", error)
        return -1


for osoba in dane_czyste_z_pliku:
    bmi_osoby = round(bmi(osoba.get("waga"), osoba.get("wzrost")))
    if bmi_osoby != -1:
        print(f"{osoba.get('imie')} {osoba.get('nazwisko')} ma BMI = {bmi_osoby}")
    else:
        print(f"{osoba.get('imie')} {osoba.get('nazwisko')} - JEST JAKIŚ PROBLEM")


# def g(a1, b, c):
#     return a1 + b + c


# def f(a, b):
#     g(a1=a, b=b, c=a)


# moduły

# __name__


# requests
# baza danych
