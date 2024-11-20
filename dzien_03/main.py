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
