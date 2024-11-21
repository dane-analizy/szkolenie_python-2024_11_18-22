def czytaj_plik(nazwa_pliku, separator=";", kodowanie="utf-8"):
    dane = []
    try:
        with open(nazwa_pliku, "r", encoding=kodowanie) as f:
            dane = [tuple(linia.strip().split(separator)) for linia in f]
    except Exception as e:
        print(e)
    return dane
