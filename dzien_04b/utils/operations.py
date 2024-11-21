from utils.file import czytaj_plik
from utils.etl import oczysc_dane

def wczytaj_czyste_dane(nazwa_pliku, separator=";", kodowanie="utf-8"):
    dane_z_pliku = czytaj_plik(nazwa_pliku, separator=separator, kodowanie=kodowanie)
    dane_czyste = oczysc_dane(dane_z_pliku)
    return dane_czyste
