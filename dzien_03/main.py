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

