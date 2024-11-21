def czytaj_plik(nazwa_pliku, separator=";", kodowanie="utf-8"):
    dane = []
    try:
        with open(nazwa_pliku, "r", encoding=kodowanie) as f:
            dane = [tuple(linia.strip().split(separator)) for linia in f]
    except Exception as e:
        print(e)
    return dane


def as_float(s):
    try:
        f = float(s)
        return f
    except Exception as e:
        print(e)
        return None


def oczysc_dane(dane):
    oczyszczone_dane = []
    for i in dane:
        oczyszczone_dane.append(
            {
                "imie": i[0],
                "nazwisko": i[1],
                "wzrost": as_float(i[2]),
                "waga": as_float(i[3]),
            }
        )
    return oczyszczone_dane


def wczytaj_czyste_dane(nazwa_pliku, separator=";", kodowanie="utf-8"):
    dane_z_pliku = czytaj_plik(nazwa_pliku, separator=separator, kodowanie=kodowanie)
    dane_czyste = oczysc_dane(dane_z_pliku)
    return dane_czyste


def bmi(masa: float, wzrost: float) -> float:
    try:
        if wzrost > 3:
            wzrost = wzrost / 100
        bmi = masa / wzrost**2
        return bmi

    except Exception as error:
        print("Błąd:", error)
        return -1
