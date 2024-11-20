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