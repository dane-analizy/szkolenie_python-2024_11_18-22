# listy

# lista_liczb = [1, 2, 3, 45, 67]
# print(lista_liczb)

# lista_napisow = ["abc", "", "cde", "ghijk"]
# print(lista_napisow)

# lista_mieszana = [1, 2, 3, "abc", "def", 5, 6, 7]
# print(lista_mieszana)

# lista może mieć elementy różnego typu
lista = [1, 2.0, 3, "abc", "def", 5, 6, 7, [1, 2, 3], ["a", "b", "c"]]
for element in lista:
    print(element, type(element))

    # czy element jest określonego typu?
    if isinstance(element, list):
        print("Element jest listą")
        for maly_element in element:
            print("\t", maly_element)

