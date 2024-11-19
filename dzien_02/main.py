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
