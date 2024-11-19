# listy

# lista_liczb = [1, 2, 3, 45, 67]
# print(lista_liczb)

# lista_napisow = ["abc", "", "cde", "ghijk"]
# print(lista_napisow)

# lista_mieszana = [1, 2, 3, "abc", "def", 5, 6, 7]
# print(lista_mieszana)

# lista może mieć elementy różnego typu
# lista = [1, 2.0, 3, "abc", "def", 5, 6, 7, [1, 2, 3], ["a", "b", "c"]]
# for element in lista:
#     print(element, type(element))

#     # czy element jest określonego typu?
#     if isinstance(element, list):
#         print("Element jest listą")
#         for maly_element in element:
#             print("\t", maly_element)

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5]
# konkretny element na liście
# print(lista[4])
# print(lista[0])

# jak długa jest lista - ile ma elementów?
# print(len(lista))

# ostatni element na liście
# print(lista[len(lista) - 1])
# print(lista[-1])

# przedostatni element na liście
# print(lista[len(lista) - 2])
# print(lista[-2])

# indeks elementu na liście - element musi istnieć
# print(lista.index(5))

# czy 5 jest na liście?
# if 5 in lista:
#     print("piątka jest na liście")


# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5]

# zakres elementów z listy
# print(lista[1:4])
# print(lista[1:100])
# print(lista[100:2000])

# zakres elementów ale co N-ty element?
# print(lista[1:100:3])

# print(lista[ :5])
# print(lista[5: ])
# print(lista[::2]) # [0:-1:2]

# # odwrócenie kolejności listy
# print(lista[::-1])

# napis = "abcdefghijkl"
# print(napis[5:9])
# print(napis[::-1])


#### ZADANIE 13

# Pobierz od użytkownika jakiś tekst/napis/słowo. Sprawdź czy jest palindromem,
# czyli czy pisane od przodu i od tyłu jest takie samo - np. sos, Anna, sedes, zaraz,
# kajak, zakaz, owocowo, potop, radar.

# tekst = input("podaj tekst: ")
# tekst = tekst.lower()
# temp = tekst[::-1]
# if tekst == temp:
#     print(f"słowo {tekst} jest palindromem!")
# else:
#     print("szukaj dalej palindromu")


# tekst = input("podaj tekst: ")
# if tekst.lower()[::-1] == tekst.lower():
#     print(f"słowo {tekst} jest palindromem!")
# else:
#     print("szukaj dalej palindromu")


# dodawanie elementów do listy
# lista = [] # ==> to jest to samo co: lista = list()
# lista.append(1)
# lista.append(2)
# lista.append(3)
# lista.append(3)
# lista.append("napis")
# print(lista)

# wstawianie w środek
# lista = [1, 2, 3, 4, 5]
# lista.insert(2, "napis") # wstawia element "napis" przed obiekt o indeksie 2
# print(lista)

# usuuwanie elementów z listy
# lista = [1, 2, 2, 3, 4, 5, 2]
# print(lista)
# lista.remove(2)
#

# wyczyszcznie listy
# lista = [1,2,3,4,5]
# lista.clear()
# print(lista)

# jak zmienić istniejący element na liście?
# lista = [1, 2, 3, 4, 5]
# print(lista)
# lista[3] = "125"
# print(lista)

# mutowalność
# lista_a = [1, 2, 3, 4, 5]
# lista_b = lista_a
# print("lista_a", lista_a)
# print("lista_b", lista_b)

# lista_a[2] = "zmieniłem ten element"
# print("lista_a", lista_a)
# print("lista_b", lista_b)


# lista_a = [1, 2, 3, 4, 5]
# lista_b = lista_a.copy()
# print("lista_a", lista_a)
# print("lista_b", lista_b)

# lista_a[2] = "zmieniłem ten element"
# print("lista_a", lista_a)
# print("lista_b", lista_b)


### ZADANIE 14

# Napisz kod który umieści w początkowo pustej liście 10 kolejnych potęg liczby 2 poprzez dodawanie ich do listy
# Następnie przeiteruj (w drugiej pętli) po tej liście i każdy z jej elementów wyświetl na konsoli w osobnej linii.


# lista_poteg_liczby_2=[]

# for element_dodawany in range(10):
#     lista_poteg_liczby_2.append(2**element_dodawany)

# for element_wyswietlany in lista_poteg_liczby_2:
#     print(element_wyswietlany)

# # to samo co ten drugi for, ale brzydkie
# for indeks in range(len(lista_poteg_liczby_2)):
#     print(lista_poteg_liczby_2[indeks])


# import random

# lista = []
# for i in range(10):
#     lista.append(random.randint(1, 20))

# print(lista)

# # sposób na złączenie 2 list
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# lista_a = l1 + l2
# print(lista_a)
# lista_b = l2 + l1
# print(lista_b)

# # kiedyś to były czasy...
# lista_c = l1.copy()
# lista_c.extend(l2)
# print(lista_c)

# lista_d = [*l2, *l1] # [ 4, 5, 6, 1, 2, 3]
# print(lista_d)


#### Zadanie 15

# Stwórz dwie listy. Każda z list ma zawierać 10 liczb losowych z zakresu 1-100.
# Połącz te dwie listy do jednej i wyświetl wynikową listę na konsoli.


# import random

# lista1 = []
# lista2 = []
# for i in range(10):
#     lista1.append(random.randint(100, 200))
#     lista2.append(random.randint(1, 99))

# lista_wynik = lista1 + lista2
# print(lista_wynik)


# _ jako symboliczna zmienna

# import random

# lista1 = []
# lista2 = []
# for _ in range(10):
#     lista1.append(random.randint(100, 200))
#     lista2.append(random.randint(1, 99))

# lista_wynik = lista1 + lista2
# print(lista_wynik)


# list-comprehention == listy składane

# klasycznie:
# lista = []
# for i in range(10):
#     lista.append(i)
# print(lista)

# lista = [i for i in range(10)]  # <- list comprehention
# print(lista)


# potegi_dwojki = [2**potega for potega in range(20)]
# print(potegi_dwojki)


### Zadanie 16

# Korzystając z list składanych wygeneruj listę 10 losowych liczb z zakresu 0-100.
# Wyświetl tę listę. Spróbuj zrobić to w jak najkrótszym zapisie.

# for iterator in iterable

# import random

# lista1 = [random.randint(1, 100) for _ in range(10)]
# print(lista1)

# # albo krócej:
# print([random.randint(1, 100) for _ in range(10)])


# zasięg zmiennej iteratora
# lista = []
# for i in range(10):
#     lista.append(i)
# print(lista)
# print(f"{i=}")

# lista = [i for i in range(10)]
# print(lista)
# print(f"{i=}")

# filtrowanie na liście składanej
# lista = []
# for i in range(50):
#     if i % 2:
#         lista.append(i)
# print(lista)


# lista = [
#     i                          <== co dodajemy listy
#     for i in range(50)         <== po czym iterujemy
#     if i % 2                   <== warunek czy dodawać
#     ]

# lista = [i for i in range(50) if i % 2]
# print(lista)



### ZADANIE 17

# Korzystając z listy składanej zbuduj listę 20 losowych liczb z przedziału 0-100.
# Następnie znowu korzystając z listy składanej zbuduj nową listę - tylko liczby parzyste z listy pierwszej.
# Wyświetl obie listy na ekranie.

# import random

# lista = [random.randint(0, 100) for _ in range(20)]
# print(lista)

# lista2 = [el for el in lista if el % 2 == 0 and el != 0]
# print(lista2)


# s = "Lady;Gaga;155;53"
# ss = s.split(";")
# print(ss)

# napis = "a.b\tcd ef"
# print(napis.split())


# osoby = open("osoby.csv", "r", encoding="utf-8").readlines()
# osoby = [osoba.strip() for osoba in osoby]
# osoby = [osoba.split(";") for osoba in osoby]

# for o in osoby:
#     print(o)


### ZADANIE 18

# Napisz program który z pliku osoby.csv wyświetli powiększone (.upper()) imię i nazwisko.

# osoby = open("osoby.csv", "r", encoding="utf-8").readlines()
# osoby = [osoba.strip() for osoba in osoby]
# osoby = [osoba.split(";") for osoba in osoby]

# for osoba in osoby:
#     imie = osoba[0].upper()
#     nazwisko = osoba[1].upper()
#     print(f"{imie}, {nazwisko} ")


# osoby = open("osoby.csv", "r", encoding="utf-8").readlines()
# osoby = [osoba.strip() for osoba in osoby]
# osoby = [osoba.split(";") for osoba in osoby]

# osoby_gotowe = []
# for osoba in osoby:
#     osoby_gotowe.append(
#         [
#             osoba[0],
#             osoba[1],
#             float(osoba[2]),
#             float(osoba[3]),
#     )
# print(osoby_gotowe)


# osoby_gotowe = [
#     [osoba[0], osoba[1], float(osoba[2]), float(osoba[3])]
#     for osoba in osoby
# ]
# print(osoby_gotowe)


### ZADANIE 19

# Napisz program który z pliku osoby.csv pobierze dane i odpowiednio dostosuje ich typy.
# Po tym niech wyliczy BMI dla każdej z osób. Wartość BMI dla osoby powinna być dodana do rekordu tej osoby.

# BMI = masa [kg] / wzrost^2 [m]

# [
#     ["Tom", "Cruise", 170.0, 68.0, BMI tomka],
#     ["Dwayne", "Johnson", 196.0, 118.0 bmi Dłejna],
#     ["Lady", "Gaga", 155.0, 53.0], BMI Gagi,
#     ["Elon", "Musk", 188.0, 90.0],
#     ["Oprah", "Winfrey", 169.0, 77.0],
#     ["Angela", "Merkel", 165.0, 72.0],
#     ["Usain", "Bolt", 195.0, 94.0],
#     ["Zac", "Efron", 173.0, 75.0],
#     ["Adele", "Adkins", 175.0, 65.0],
#     ["Danny", "DeVito", 147.0, 70.0],
# ]


# osoby = [osoba.strip().split(";") for osoba in open("osoby.csv", "r", encoding="utf-8")]

# osoby_bmi = [
#     [
#         osoba[0],  # imie
#         osoba[1],  # nazwisko
#         float(osoba[2]),  # float ze wzrostu
#         float(osoba[3]),  # float z wagi
#         float(osoba[3]) / (float(osoba[2]) / 100) ** 2,  # wyliczenie bmi
#     ]
#     for osoba in osoby
# ]

# print(osoby_bmi)


# osoby = [
#     [
#         osoba[0],
#         osoba[1],
#         float(osoba[2]),
#         float(osoba[3]),
#         round(float(osoba[3]) / ((float(osoba[2]) / 100) ** 2), 2),
#     ]
#     for osoba in [
#         osoba.strip().split(";") for osoba in open("osoby.csv", "r", encoding="utf-8")
#     ]
# ]

# print(osoby)


# # sortowanie
# lista = [45, 12, 90, 67, 83]
# print(lista)

# lista_posortowana = sorted(lista)
# print(lista_posortowana)

# # lista_posortowana_odwrotnie = sorted(lista)[::-1]
# lista_posortowana_odwrotnie = sorted(lista, reverse=True)
# print(lista_posortowana_odwrotnie)

# sortowanie listy "w miejscu" - ze zmianą samej listy
# lista.sort()
# print(lista)

# lista.sort(reverse=True)
# print(lista)

# import pandas as pd

# dataframe = pd.DataFrame(
# [
#     ["Tom", "Cruise", 170.0, 68.0],
#     ["Dwayne", "Johnson", 196.0, 118.0],
#     ["Lady", "Gaga", 155.0, 53.0],
#     ["Elon", "Musk", 188.0, 90.0],
#     ["Oprah", "Winfrey", 169.0, 77.0],
#     ["Angela", "Merkel", 165.0, 72.0],
#     ["Usain", "Bolt", 195.0, 94.0],
#     ["Zac", "Efron", 173.0, 75.0],
#     ["Adele", "Adkins", 175.0, 65.0],
#     ["Danny", "DeVito", 147.0, 70.0],
# ], columns=['imie', 'nazwisko', 'wzrost', 'waga'])

# print(dataframe)

# dataframe["bmi"] = dataframe["waga"] / (dataframe["wzrost"]/100)**2
# print(dataframe)


# sortowanie ciąg dalszy
# lista = [1, 2, "abc", "efg", 5, 10] # <- to sie nie uda
# print(sorted(lista))

# lista = [[4, 1], [2, 3], [1, 4], [3, 2]]
# # print(sorted(lista))

# # print(sorted(lista, key=lambda para: para[1]))

# def wybieracz(element):
#     return element[1]

# print(sorted(lista, key=wybieracz))


# print(sorted(lista, key=lambda para: para[1], reverse=True))


#### ZADANIE 20

# Korzystając z kodu z Zadania 19 zbuduj listę zawodników z ich BMI oraz posortują ją na dwa sposoby (wypisz wyniki sortowania):
# 1. wg nazwiska (alfabetycznie A-Z)
# 2. wg BMI malejąco


# osoby = [osoba.strip().split(";") for osoba in open("osoby.csv", "r", encoding="utf-8")]
# osoby = [
#     [
#         osoba[0],
#         osoba[1],
#         float(osoba[2]),
#         float(osoba[3]),
#         float(osoba[3]) / ((float(osoba[2]) / 100) ** 2),
#     ]
#     for osoba in osoby
# ]

# print(f"sortowanie wg nazwiska rosnąco:")
# osoby_gotowe = sorted(osoby, key=lambda osoba: osoba[1])
# for osoba in osoby_gotowe:
#     print(osoba)

# print(f"sortowanie wg BMI malejąco:")
# osoby_gotowe = sorted(osoby, key=lambda osoba: osoba[4], reverse=True)
# for osoba in osoby_gotowe:
#     print(osoba)


# join() -> łączenie listy w string

# lista = [
#     "janek",
#     "marek",
#     "zdzichu",
#     "tomek",
# ]  # docelowo chcemy: "janek,marek,zdzichu,tomek"
# wynikowy_str = ""
# SEP = ","
# iteracja = 0
# for el in lista:
#     iteracja += 1
#     if iteracja == 1:
#         wynikowy_str = el
#     if iteracja >= 2:
#         wynikowy_str = wynikowy_str + SEP + el
# print(wynikowy_str)

# enumerate
# lista = [
#     "janek",
#     "marek",
#     "zdzichu",
#     "tomek",
# ]
# for iteracja, el in enumerate(lista, start=1):
#     print(iteracja, el)


# lista = [
#     "janek",
#     "marek",
#     "zdzichu",
#     "tomek",
# ]

# SEP = ","
# for iteracja, el in enumerate(lista):
#     if iteracja == 0:
#         wynikowy_str = el
#     else:
#         wynikowy_str = wynikowy_str + SEP + el
# print(wynikowy_str)


# lista = [
#     "janek",
#     "marek",
#     123,
#     "zdzichu",
#     "tomek",
# ]

# lista = [str(e) for e in lista]
# SEP = ","
# wynikowy_str = SEP.join(lista)
# # wynikowy_str = SEP.join([str(e) for e in lista])
# print(wynikowy_str)


#### ZADANIE 21

# Korzystając z kodu z Zadania 20 zbuduj listę stringów zbudowaną z informacji o osobach z wyliczonym BMI
# posortowaną wg nazwiska (alfabetycznie A-Z).
# Przykładowy element na liście to string: "Imie;Nazwisko;wzrost;waga;bmi"

# SEP = ";"

# osoby = [osoba.strip().split(SEP) for osoba in open("osoby.csv", "r", encoding="utf-8")]
# osoby = [
#     [
#         osoba[0],
#         osoba[1],
#         float(osoba[2]),
#         float(osoba[3]),
#         float(osoba[3]) / ((float(osoba[2]) / 100) ** 2),
#     ]
#     for osoba in osoby
# ]
# osoby_posortowane = sorted(osoby, key=lambda osoba: osoba[1], reverse=True)

# lista_wynikowa = []
# for osoba in osoby_posortowane:
#     osoba_str = [str(el) for el in osoba]
#     lista_wynikowa.append(SEP.join(osoba_str))

# # lista_wynikowa = [SEP.join([str(el) for el in osoba]) for osoba in osoby_posortowane]
# print(lista_wynikowa)


# krotki - po angielsku: tuple
# krotka = (1, 2, 3, "abc", 12.34, [1, 2], ["a", "b"])
# print(krotka)
# # lista z tupla
# lista = list(krotka)
# print(lista)

# tupel z listy
# lista  = [1, 2, 3, "abc", 12.34, [1, 2], ["a", "b"]]
# print(lista)
# krotka = tuple(lista)
# print(krotka)

# krotka_jednoelementowa = (123, )
# k = ("napis", 13414, "daf")
# print(k)
# a,b,c = 1,2,3
# print(a)
# print(b)
# print(c)


# a = 10
# b = 0
# print(f"{a=} {b=}")

# temp = a
# a = b
# b = temp
# print(f"{a=} {b=}")

# a,b = b,a
# print(f"{a=} {b=}")

# krotka = (1, 2, 3, 4, 5)
# # print(krotka[2])
# # print(krotka[-1])
# # print(krotka[2:4])

# print(sorted(krotka, reverse=True))  # <- zwróci posortowaną listę
# print(tuple(sorted(krotka, reverse=True)))  # <- zwróci posortowaną krotkę

# nie ma tuple-coprehention / krotki składane
# import random

# l = [random.randint(1, 100) for _ in range(10)]
# k = tuple(l)
# print(l)
# print(k)


#### ZADANIE 22

# Zbuduj krotkę zawierającą losowo wygenerowane 20 liczb posortowanych rosnąco.
# import random

# krotka = [random.randint(1, 100) for i in range(20)]
# krotka = tuple(sorted(krotka))
# print(krotka)

# dodawanie krotek
# kr1 = (1,1,23,4)
# kr2 = (7,8,9,1)
# kr3 = kr1+kr2
# print(kr3)


# s = (1, 23, 45)
# print(s)
# print(*s)

# a, b, c = s
# print(b)


# lista plików i katalogów
# import os

# KATALOG_STARTOWY = "."

# for s in os.walk(KATALOG_STARTOWY):
#     # print(s)
#     # s -> nazwa aktualnego folderu
#     #      lista folderów w środku
#     #      lista plików w środku
#     current_path, folders, files = s

#     print(f"\nZawartość '{current_path}':")
#     if folders:
#         for folder in folders:
#             print(f"\t - {folder} [KATALOG]")
#     else:
#         print("\tNie ma katalogów")

#     if files:
#         for file in files:
#             pelna_sciezka = os.path.join(current_path, file)
#             print(f"\t - {file} [PLIK]")
#             print(f"\t   {pelna_sciezka}")
#     else:
#         print("\tNie ma plików")


# można dadać element
# if file.endswith(".txt"):
#     # wczytaj plik
#     # znajdz w nim ciąg znaków
#     # wyświetl numer linii gdzie był ten ciąg znaleziony


# zbiory = set

# lista = [1, 1, 2, 2, 3, 3, 4, 5, 6, 7]
# zbior = set(lista)
# print(lista)
# print(zbior)

# lista_a = list(zbior)
# print(lista_a)

# lista unikalnych elementów listy
# lista = [1, 1, 2, 2, 3, 3, 4, 5, 6, 7]
# lista = list(set(lista))

# l = [1, 1, "a", "b", "a", "b"]
# s = set(l)
# print(l)
# print(s)


# l = [1, 1, "a", "b", "a", "b", (1,2,3), (2,3,4)]
# s = set(l)
# print(l)
# print(s)


# s1 = {1,2,3}
# s2 = {1,3,5,6}

# # s1.add(4)
# # print(s1)

# print(s1.intersection(s2))
# print(s1.union(s2))

# print(s1.difference(s2))
# print(s2.difference(s1))

# print(len(s2))
