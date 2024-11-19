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