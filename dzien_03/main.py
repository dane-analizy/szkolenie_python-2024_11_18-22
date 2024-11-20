# wyszukiwanie ciągu znaków w plikach
# https://wolnelektury.pl/media/book/txt/pan-tadeusz.txt
# ile razy w tekście Pana Tadeusza występuje słowo "Tadeusz" (bez względu na wielkość liter)

# nazwa_pliku = "pan-tadeusz.txt"
# enc = "utf-8"

# poszukiwany_ciag = "tadeusz"

# tekst = open(nazwa_pliku, "r", encoding=enc).read()
# tekst = tekst.lower()
# print(tekst.count(poszukiwany_ciag))


# wypisz linie w których występuje podany ciąg

# nazwa_pliku = "pan-tadeusz.txt"
# enc = "utf-8"
# poszukiwany_ciag = "tadeusz"

# for numer_linii, linia in enumerate(open(nazwa_pliku, "r", encoding=enc), start=1):
#     tekst = linia.strip().lower()
#     ile_wystapien = tekst.count(poszukiwany_ciag)
#     if ile_wystapien:
#         print(
#             f"{numer_linii:>6} | {ile_wystapien:>2} : {tekst.replace(poszukiwany_ciag, '['+poszukiwany_ciag+']')}"
#         )


# zadanie z pathlib.Path() + szukanie instrukcji pythona

# from pathlib import Path

# p = Path("..")

# enc = "utf-8"
# poszukiwany_ciag = "count"

# for plik in p.rglob("*"):
#     # pominięcie zawartości katalogi .git
#     # if plik.as_posix().startswith("../.git/"):
#     #     continue
#     if plik.is_file():
#         for numer_linii, linia in enumerate(open(plik, "r", encoding=enc), start=1):
#             tekst = linia.strip().lower()
#             ile_wystapien = tekst.count(poszukiwany_ciag)
#             if ile_wystapien:
#                 print(
#                     f"{plik.as_posix()} | {numer_linii:>6} | {ile_wystapien:>2} : {linia.rstrip()}"
#                 )


#### ZADANIE 23

# Napisz program który będzie pobierał nazwę pliku z kodem w Pythonie.
# Program będzie wyświetlał wszystkie linie które **nie** są komentarzami i nie są puste,
# razem z numerem linii.


# nazwa_pliku = "main.py"
# enc = "utf-8"

# for numer_linii, linia in enumerate(open(nazwa_pliku, "r", encoding=enc), start=1):
#     tekst = linia.strip()

#     if tekst != "" and not tekst.startswith("#"):
#         print(f"{numer_linii:>4} | {linia.rstrip()}")


# tekst = "ala ma X"
# if tekst and len(tekst) >= 10 and tekst[10] == "a":
#     print("Tekst nie jest pusty i 'a' jest pod indeksem 10")
# else:
#     print("If dla false")


# zapisywanie do pliku
# nazwa_pliku_out = "osoby_2.csv"
# nazwa_pliku_out_2 = "osoby_3.csv"
# nazwa_pliku_out_3 = "osoby_4.csv"

# lista = ['pierwsza linia', 'lina druga', 'oraz trzecia linia']
# napis = "to jest napis który zapiszemy do pliku"

# plik = open(nazwa_pliku_out, "w", encoding="utf-8")
# plik.write(napis)
# plik.close()

# plik = open(nazwa_pliku_out_2, "w", encoding="utf-8")
# lista_do_zapisu = [element+'\n' for element in lista]
# plik.writelines(lista_do_zapisu)
# plik.close()

# plik = open(nazwa_pliku_out_3, "w", encoding="utf-8")
# zawartosc_do_zapisu = "\n".join(lista)
# plik.write(zawartosc_do_zapisu)
# plik.close()


# context-manager

# lista = ["pierwsza linia", "lina druga", "oraz trzecia linia"]
# nazwa_pliku = "plik_wyjsciowy.txt"

# # plik = open(nazwa_pliku, "w", encoding="utf-8")
# with open(nazwa_pliku, "w", encoding="utf-8") as plik:
#     print("plik w ramach with:", plik)
#     print(plik.writable())
#     lista_do_zapisu = [element+'\n' for element in lista]
#     plik.writelines(lista_do_zapisu)

# print("plik po with:", plik)
# print(plik.writable())


### ZADANIE 24

# Przepisz zawartość pliku osoby.csv do results.csv linia po linii.

# nazwa_pliku = "osoby.csv"
# nazwa_pliku2 = "results.csv"

# with open(nazwa_pliku, "r", encoding="utf-8") as plik:
#     with open(nazwa_pliku2, "w", encoding="utf-8") as plik2:
#         for linia in plik.readlines():
#             plik2.writelines(linia)


# inne podejście

# nazwa_pliku = "osoby.csv"
# nazwa_pliku2 = "results_2.csv"

# osoby = open(nazwa_pliku, "r", encoding="utf-8").readlines()

# plik = open(nazwa_pliku2, "w", encoding="utf-8")
# for osoba in osoby:
#     plik.write(osoba)

# plik.close()


# inne podejście:

# nazwa_pliku = "osoby.csv"
# nazwa_pliku2 = "results.csv"
# osoby = open(nazwa_pliku, "r", encoding="utf-8").readlines()
# with open(nazwa_pliku2, "w", encoding="utf-8") as plik2:
#     plik2.writelines(osoby)


#### ZADANIE 25

# Przepisz plik 'zawodnicy.csv' do pliku 'zawodnicy_clean.csv' zmieniając:
# - zamień ; na ,
# - usuń powtórzone linie

# nazwa_pliku_in = "zawodnicy.csv"
# s = open(nazwa_pliku_in, "r", encoding="utf-8").read()
# print(s)

# nazwa_pliku_in = "zawodnicy.csv"
# with open(nazwa_pliku_in, "r", encoding="utf-8") as p:
#     s = p.read()
# print(s)


# enc = "utf-8"
# nazwa_pliku = "zawodnicy.csv"
# nazwa_pliku2 = "zawodnicy_clean.csv"

# zawodnicy = open(nazwa_pliku, "r", encoding="utf-8").readlines()
# zawodnicy = [linia.strip() for linia in zawodnicy]
# zawodnicy = set(zawodnicy)
# zawodnicy = [zawodnik.replace(";", ",") + "\n" for zawodnik in zawodnicy]
# zawodnicy.sort()

# with open(nazwa_pliku2, "w", encoding="utf-8") as zawodnicy_clean:
#     zawodnicy_clean.writelines(zawodnicy)


# pakiet zewnętrzny - instalacja
# pip install nazwa_pakietu

# from faker import Faker

# fake = Faker(locale="pl")
# print(fake.name())
# print(fake.first_name())
# print(fake.last_name())
# print(fake.company())
# print(fake.email())
# print(fake.phone_number())
# print(fake.city())
# print(fake.street_name())
# print(fake.building_number())
# print(fake.zipcode())


### ZADANIE 26

# Korzystając z pakietu Faker wygeneruj plik CSV zawierający 10 tysięcy rekordów zawierających:
# id będące kolejną liczbą, imię, nazwisko, nazwa firmy, email, telefon, miasto

# from faker import Faker

# fake = Faker(locale="pl")
# with open("spoleczenstwo.csv", "w", encoding="utf-8") as plik:
#     for id in range(10_000):
#         plik.write(
#             f"{id+1};"
#             + f"{fake.first_name()};"
#             + f"{fake.last_name()};"
#             + f"{fake.company()};"
#             + f"{fake.email()};"
#             + f"{fake.phone_number()};"
#             + f"{fake.city()}"
#             + "\n"
#         )


# słowniki

# int()
# float()
# str()
# list()
# tuple()
# set()
# dict()

# d = {}
# d = {
#     "klucz_int": 1234,
#     "klucz_float": 123.567,
#     "klucz_lista": [1, 2, 3, "abc"],
#     "klucz_slownik": {"a": 1, "b": "napis"},
# }
# print(d)

# print(d["klucz_int"], type(d["klucz_int"]))
# print(type(d))

# lista kluczy
# print(d.keys())
# print(d["klucz_slownik"].keys())

# lista wartości
# print(d.values())
# print(d['klucz_slownik'].values())

# for klucz in d.keys():
#     print(f"{klucz=}, wartość: {d[klucz]}")


# d = {
#     "klucz_int": 1234,
#     "klucz_float": 123.567,
#     "klucz_lista": [1, 2, 3, "abc"],
#     "klucz_slownik": {"a": 1, "b": "napis"},
# }

# # print(d.items())

# for k,v in d.items():
#     print(f"klucz={k}, wartość={v}")


# d = {
#     19: "wtorek",
#     (2024, 11, 20): "środa",
#     # [1,2]: "to nie zadziała"
# }

# print(d)
# print(d[19])

# d[20] = "nowa wartość"
# print(d)

# d[19] = ["to", "zostało", "zmienione"]
# print(d)

# d = {
#     "a": 1,
#     "b": 2,
#     "c": 3
# }

# if "e" in d.keys():
#     print("e JEST na liście kluczy")
# else:
#     print("e NIE jest na liście kluczy")

# # print(d["e"])
# print(d.get("e"))
# print(d.get("g", "nie mam pańskiego płaszcza"))


#### ZADANIE 27

# Wczytaj dane z pliku osoby.csv i utwórz z nich słownik.
# Kluczem niech będzie krotka stworzona z imienia i nazwiska,
# a wartością słownik stworzony z wagi i wzrostu (z odpowiednimi kluczami).
# Wyświetl kolejne elementy słownika w konsoli.

# {
#     ("Tom", "Cruise"): {"waga": 68, "wzrost": 170},
#     ("Lady", "Gada"): {"waga": 68, "wzrost": 170},
# }


# osoby = open("osoby.csv").readlines()
# osoby = [o.strip().split(";") for o in osoby]

# dane_osob = {} # równoznaczne z: dane_osob = dict()

# for osoba in osoby:
#     klucz = (osoba[0], osoba[1])
#     wartosc = {"wzrost":float(osoba[2]), "waga":float(osoba[3])}
#     dane_osob[klucz] = wartosc

# for klucz, wartosc in dane_osob.items():
#     print(f"{klucz}, {wartosc}")


# print(dane_osob)


# nazwa_pliku = "osoby.csv"
# osoby = open(nazwa_pliku, "r", encoding="utf-8").readlines()
# osoby = [o.strip().split(";") for o in osoby]

# d = {}
# for imie, nazwisko, wzrost, waga in osoby:
#     d[(imie, nazwisko)] = {"wzrost": wzrost, "waga": waga}

# print(d)


# lista krotek zrzutowana na słownik
# >>> k = [(1, "a"),(2, "b"), (3, "c")] 
# >>> k
# [(1, 'a'), (2, 'b'), (3, 'c')]
# >>> dict(k)
# {1: 'a', 2: 'b', 3: 'c'}


# dict-comprehention

# lista = [ element for element in iterable ]


# nazwa_pliku = "osoby.csv"
# osoby = open(nazwa_pliku, "r", encoding="utf-8").readlines()
# osoby = [o.strip().split(";") for o in osoby]

# slownik = {element[0]: element[1] for element in osoby if int(element[2])>170}
# print(slownik)


#### ZADANIE 28

# Policz ile razy występują poszczególne słowa w tekście "Pana Tadeusza".
# Użyj słowników - kluczem niech będzie słowo zapisane małymi literami,
# a wartością - liczba jego wystąpień.
# Wyświetl wszystkie elementy ze słownika, których klucz zaczyna się od "tadeusz".


# tekst = open("pan-tadeusz.txt", encoding="utf-8").read()
# tekst = tekst.lower()

# # usunąć zbędne znaki typu .,/?
# # tekst = tekst.replace("\n", " ")
# # tekst = tekst.replace(".", " ")
# # tekst = tekst.replace(",", " ")
# # tekst = tekst.replace("!", " ")
# # tekst = tekst.replace("?", " ")

# zakazane_znaki = ',.?!\n-:;…—*()%-+"«»/'
# for bz in zakazane_znaki:
#     tekst = tekst.replace(bz, " ")

# # tekst rozbić na słowa => .split()
# tekst = tekst.split()

# # utworzyć pusty słownik
# licznik_slow = {}

# # w pętli po rozbitych słowach aktualizować (dodawać albo zmieniać) krotność wystąpień
# for slowo in tekst:
#     # if slowo in licznik_slow.keys():
#     #     licznik_slow[slowo] +=1
#     # else:
#     #     licznik_slow[slowo] = 1
#     licznik_slow[slowo] = licznik_slow.get(slowo, 0) + 1

# for slowo, liczba in licznik_slow.items():
#     if slowo.startswith("tadeusz"):
#         print(f"{slowo}: {liczba}")


# print(sorted(licznik_slow)) # -> to nam posortuje tylko klucze i nie zwróci wartości

# tekst = open("pan-tadeusz.txt", encoding="utf-8").read()
# tekst = tekst.lower()

# zakazane_znaki = ',.?!\n-:;…—*()%-+"«»/'
# for bz in zakazane_znaki:
#     tekst = tekst.replace(bz, " ")

# tekst = tekst.split()

# licznik_slow = {}
# for slowo in tekst:
#     if len(slowo) > 4: # pozybcie się słów typu że, o, nad, w
#         licznik_slow[slowo] = licznik_slow.get(slowo, 0) + 1


# lista_posortowanych_krotek_ze_slownika = sorted(licznik_slow.items(), key=lambda kv:kv[1])
# licznik_slow_posortowany = { k[0]:k[1] for k in lista_posortowanych_krotek_ze_slownika }
# albo:
# licznik_slow_posortowany = dict(   sorted(licznik_slow.items(), key=lambda kv:kv[1])   )
# # print(licznik_slow_posortowany)


# for k,v in licznik_slow_posortowany.items():
#     if k.startswith("tadeusz"):
#         print(k,v)


# import time


# tekst = open("pan-tadeusz.txt", encoding="utf-8").read()
# tekst = tekst.lower()

# zakazane_znaki = ',.?!\n-:;…—*()%-+"«»/'
# for bz in zakazane_znaki:
#     tekst = tekst.replace(bz, " ")

# tekst = tekst.split()

# start_time = time.perf_counter()
# tekst_unikalne = set(tekst)
# licznik_slow = {}
# for slowo in tekst_unikalne:
#     zliczenie = tekst.count(slowo)
#     licznik_slow[slowo] = zliczenie
# end_time = time.perf_counter()


# for k, v in licznik_slow.items():
#     if k.startswith("tadeusz"):
#         print(k, v)

# print(end_time-start_time)


# import time

# tekst = open("pan-tadeusz.txt", encoding="utf-8").read()
# tekst = tekst.lower()

# zakazane_znaki = ',.?!\n-:;…—*()%-+"«»/'
# for bz in zakazane_znaki:
#     tekst = tekst.replace(bz, " ")

# tekst = tekst.split()

# start_time = time.perf_counter()
# licznik_slow = {}
# for slowo in tekst:
#     licznik_slow[slowo] = licznik_slow.get(slowo, 0) + 1
# end_time = time.perf_counter()


# for k, v in licznik_slow.items():
#     if k.startswith("tadeusz"):
#         print(k, v)

# print(end_time - start_time)




# import time
# from collections import Counter

# tekst = open("pan-tadeusz.txt", encoding="utf-8").read()
# tekst = tekst.lower()

# zakazane_znaki = ',.?!\n-:;…—*()%-+"«»/'
# for bz in zakazane_znaki:
#     tekst = tekst.replace(bz, " ")

# tekst = tekst.split()

# start_time = time.perf_counter()
# licznik_slow = Counter(tekst)
# end_time = time.perf_counter()

# print(licznik_slow)
# print(type(licznik_slow))

# for k, v in licznik_slow.items():
#     if k.startswith("tadeusz"):
#         print(k, v)

# print(end_time - start_time)



### wyjątki

# try..catch <- java
# try..except <- python

# a = 10
# b = 0
# wynik = a / b
# print(wynik)


# a = 10
# b = 0
# try:
#     wynik_ba = b/a
#     print("udało się b/a")
#     print(wynik_ba)

#     wynik_ab = a / b
#     print("udało się a/b")
#     print(wynik_ab)

# except:
#     print("błąd")

# print("koniec")


# a = 14
# b = 3

# try:
#     w = a/b
#     print(w)
# except Exception as e:
#     print(e)
#     print(type(e))


    
# a = 14
# b = "agwg"

# try:
#     w = a / b
#     print(w)
# except ZeroDivisionError:
#     print("Nie dzielimy przez zero, ziomuś!")
# except TypeError:
#     print("No ale dziel to co się da dzielić!")
# except Exception:
#     print("Inny błąd")


# a = 14
# b = 14

# try:
#     w = a / b
#     print(w)
#     raise NotImplementedError
# except ZeroDivisionError:
#     print("Nie dzielimy przez zero, ziomuś!")
# except TypeError:
#     print("No ale dziel to co się da dzielić!")
# except Exception as e:
#     print("Inny błąd:", e, type(e))

# # def dzielenie(a,b):
# #     if b ==0:
# #         raise ZeroDivisionError
# #     else:
# #         return a/b

# s = input("Daj liczbę: ")
# try:
#     licza = float(s)
#     print(licza*2)
# except Exception as e:
#     print("Ale to miała być liczba...")
#     print(f"Błąd: {e} ({type(e)})")

# print("Skończyłem")

# def as_float(s):
#     try:
#         ss = float(s)
#     except:
#         ss = None
#     return ss

# as_float(input())
