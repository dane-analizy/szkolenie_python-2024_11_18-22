# moduły = zbiory funkcji w oddzielnym pliku
# zobacz plik "narzedzia.py"

# from narzedzia import bmi
# from narzedzia import as_float

# wynik = bmi(80, 180)
# print(wynik)

# print(as_float("124.515"))


# uwaga - kod w importowanych rzeczach się wykonuje
# import modul_test

# modul_test.hello("Łukasz")
# print(modul_test.zmienna_x)


# __name__

# print(__name__)  # __main__

# import modul_dwa # <- cały plik modul_dwa.py się wykona

# if __name__ == "__main__":
#     print("uruchomiłeś mnie (jestem main.py)")
    
    


# tradycyjna struktura kodu:

# import time
# import json

# import yaml

# from narzedzia import bmi

# STALA = 12345

# def funkcja():
#     """Nic nie robi, bo to przykład"""
#     pass

# def main():
#     # tutaj główny kod programu 
#     pass

# if __name__ == '__main__':
#     main()


# pakiety

# import utils.etl 

# print(utils.etl.as_float("124"))


from utils.operations import wczytaj_czyste_dane
from utils.calc import bmi

dane = wczytaj_czyste_dane("osoby.csv")

for o in dane:
    print(f"{o['imie']}: BMI = {bmi(o['waga'], o['wzrost'])}")


# requests
