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


def bmi(masa: float | int, wzrost: float | int) -> float:
    try:
        if wzrost > 3:
            wzrost = wzrost / 100
        bmi = masa / wzrost**2
        return bmi
    except Exception as error:
        print("Błąd:", error)
        return -1


print(bmi(80, "180"))
print(bmi(80, 180))


# requests
# baza danych
