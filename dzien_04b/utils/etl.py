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
