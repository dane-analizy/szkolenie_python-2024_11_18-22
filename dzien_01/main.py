# print("Dzień dobry")

# print("Dzień dobry")
# print("Dzień dobry")
# print("Dzień dobry")
# print("Dzień dobry")
# print("Dzień dobry")
# print("Dzień dobry")

# for a in range(10):
#     print("Dzień dobry")
#     print("Dzień dobry")

#     for a in range(10):
#         print("Dzień dobry")
#         print("Dzień dobry")
# print("Dzień dobry")

# # nazwy zmiennych
# kwotapodatku
# KwotaPodatku
# kwotaPodatku <- tak lubi Java
# kwota_podatku # <- tak powinno być w pythonie
# Kwota_Podatku

# # nazwy stałych
# KWOTA_PODATKU


# nazwy klas
# class MojaKlasa

# nazwy funkcji
# def to_jest_funkcja(param1, param2):

# print("kot ma ale")
# print = 12
# print("ala ma kota")


# ZMIENNE

# definicje - tworzymy zmienną i nadajemy jej wartość
# zmienna_int = 123
# zmienna_float = 3.1415
# zmienna_znak = "a"
# zmienna_napis = "ala ma kota"

# # wyświetlamy wartości zmiennych
# # print(zmienna_int)
# # print(zmienna_float)
# # print(zmienna_znak)
# # print(zmienna_napis)

# print("zmienna_int", zmienna_int)
# print("zmienna_float", zmienna_float)
# print("zmienna_znak", zmienna_znak)
# print("zmienna_napis", zmienna_napis)

# # zmienna_napis = 56789
# # print("zmienna_napis", zmienna_napis)

# # print(type(zmienna_znak))
# # print(type(zmienna_napis))

# # zmienna_nowa = zmienna_int + zmienna_float
# # zmienna_nowa = zmienna_int + 20
# zmienna_nowa = zmienna_float + 10
# print(type(zmienna_nowa))

# a = 10
# s = "ala ma kota"
# # print(a+s)
# # print(a,s, "1111 ", "2222", "3333")

# # f-sting
# napis = f"ALA MA KOTA: {s} {a}{a}"
# print(napis)

# pobieranie informacji od użytkownika

# a = 123
# b = -60
# wynik = a + b
# print(f"Wynik dodawania a+b={wynik}")

# dane_od_uzytkownika = input("Podaj coś:")
# print(dane_od_uzytkownika)


### ZADANIE 1

# Napisz program, który pobierze od użytkownika imię i nazwisko (jako dwa pytania),
# a potem wypisze w konsoli pozdrowienie "Witaj IMIĘ NAZWISKO!"

# imie = input("Podaj imię: ")
# nazwisko = input("Podaj nazwisko")
# print(f"Witaj {imie} {nazwisko}!")

# stringi można mnożyć przez liczbę
# napis = "abc"
# print(napis * 20)


### ZADANIE 2

# Napisz kalkulator dodający dwie liczby pobrane od użytkownika.


# a = input("podaj pierwszą liczbę: ")
# b = input("podaj drugą liczbę: ")

# a = float(a)
# b = float(b)

# print(type(a))
# c = a + b
# print(type(c))
# print(f"Wynik dodawania {a} + {b} = {c}")


# Definicja wskaźnika BMI https://pl.wikipedia.org/wiki/Wska%C5%BAnik_masy_cia%C5%82a
# BMI = masa [kg] / wzrost^2 [m]

### ZADANIE 3

# Napisz program, który pobierze od użytkownika masę i wzrost,
# a następnie policzy BMI i wypisze wynik na konsolę.

# potęgowanie w pythonie:
# x**y => x do potęgi y
# pow(x, y) => x do potęgi y

# masa = input("Podaj mase ciała w kg: ")
# wzrost = input("Podaj wzrost w metrach: ")
# masa = float(masa)
# wzrost = float(wzrost)
# bmi = masa / (wzrost**2)
# bmi = round(bmi, 2)
# print(f"Twój wskaźnik BMI wynosi {bmi}")

# kwota_wolna_od_podatku = 123
# gwgg = kwota_wolna_od_podatku**2
# adg = kwota_wolna_od_podatku - 10

# kwota_wolna_od_podatku


### INSTRUKCJE WARUNKOWE

# a = 0
# if a > 0:
#     print(f"Liczba a={a} jest dodatnia")
#     print("Druga linia bloku pod if")
#     print("A tu jeszcze coś")

# if a < 0:
#     print(f"Liczba a={a} jest ujemna")

# if a == 0:
#     print("a jest zerem")

# print("To już jest po ifie")


# a = 0
# if a > 0:
#     print(f"Liczba a={a} jest dodatnia")
#     print("Druga linia bloku pod if")
#     print("A tu jeszcze coś")
# else:
#     print("a nie jest dodatnie")

# print("To już jest po ifie")


# a = -10
# if a > 0:
#     print(f"Liczba a={a} jest dodatnia")
#     print("Druga linia bloku pod if")
#     print("A tu jeszcze coś")
# elif a < 0:
#     print(f"Liczba a={a} jest ujemna")
# else:
#     print("a jest zerem")

# print("To już jest po ifie")

# != -> nie-równe


# a =1234
# if a > 1:
#     print("costam")
# else:
#     pass # instrukcja która ni nie robi

# def f():
#     pass


# ciekawostki związane z f-stringami

# liczba = 123.456789
# print(f"{liczba}")

# if kraj == "polska":
#     numer = f"+48 {numertelefonu}"

# napis = f"{liczba}"
# print(napis)

# print(f"{liczba:.2f}")

# print(f"{1/3:.6f}")
# print(f"{1/3:%}")
# print(f"{1/3:.1%}")

# napis = "Jasio"
# print(f"|{napis:<20}|")
# print(f"|{napis:>20}|")
# print(f"|{napis:^20}|")

# print(f"|{1/3:^20.1%}|")


### ZADANIE 4

# Niech użytkownik poda jakąś liczbę. W odpowiedzi wyświetlamy tę liczbę
# i informację czy liczba jest dodatnia, ujemna czy też jest zerem.

# zmienna = float(input("podaj dowolną liczbę: "))
# informacja = ""

# if zmienna > 0:
#     informacja = "jest dodatnia"
# elif zmienna == 0:
#     informacja = "jest równa 0"
# elif zmienna < 0:
#     informacja = "jest ujemna"
# else:
#     informacja = "nie jest liczbą, podaj liczbę"

# print(f"podałeś: zmienna={zmienna}, {informacja}")
# print(f"podałeś: {zmienna=}, {informacja}")


### ZADANIE 5

# Napisz program, który pobierze od użytkownika masę i wzrost,
# a następnie policzy BMI i wypisze na konsolę.
# Dodatkowo - na podstawie wartości obliczonego BMI niech poda komentarz.
# < 16 => wygłodzenie
# 16 - 17 włącznie => wychudzenie
# 17 - 18,49 => niedowaga
# 18,5 - 24,999 => pożądana masa ciała
# 25 - 29,999 => nadwaga
# 30 - 34,999 => otyłość I stopnia
# 35 - 39,999 => otyłość II stopnia (duża)
# > 40 otyłość III stopnia (chorobliwa)


# weight = input("Podaj masę [kg]: ")
# weight = float(weight)

# height = input("Podaj wzrost [cm]: ")
# height = float(height) / 100

# bmi = weight / height**2

# if bmi <= 16:
#     bmi_comment = "wygłodzenie"
# elif bmi <= 17:
#     bmi_comment = "wychudzenie"
# elif bmi <= 18.5:
#     bmi_comment = "niedowagę"
# elif bmi <= 25:
#     bmi_comment = "pożądaną masa ciała"
# elif bmi <= 30:
#     bmi_comment = "nadwagę"
# elif bmi <= 35:
#     bmi_comment = "otyłość I stopnia"
# elif bmi <= 40:
#     bmi_comment = "otyłość II stopnia (duża)"
# else:
#     bmi_comment = "otyłość III stopnia (chorobliwa)"

# print(
#     f"\nTwój wynik BMI:\n- przy wzroście {height} cm\n- wadze {weight} kg\nto {bmi:.2f}, co oznacza {bmi_comment}"
# )


# (16 <= bmi) and (bmi < 17)
# 16 <= bmi < 17


### PĘTLE

# od 0 do 10, ale bez 10
# for i in range(10):
#     # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#     print(f"{i=}")

# od 5 do 10, ale bez 10
# for i in range(5, 10):
#     print(f"{i=}")

# od 2 do 20, co 3, ale bez 20
# for i in range(2, 20, 3):
#     print(f"{i=}")

# range() zwraca obiekt typu "iterable"
# przechodzimy po pętli iteratorem

# napis = "abcdefghijk"
# for litereka in napis:
#     print(litereka)


### ZADANIE 6

# Wyświetl 20 kolejnych potęg liczby 2 (od 2^0 do 2^19).

# for potega in range(20):
#     wynik = 2**potega
#     print(f"2^{potega} = {wynik}")


# for i in range(20):
#     print(f"2^{i}={2**i}")


# # reszta "r" z dzielenia "x przez y": r = x % y
# print(4%2)
# print(4 % 3)

# # wartość całkowita z dzielenia X przez Y
# print(11 // 3)
# print(11 % 3)


### ZADANIE 7

# Wydrukuj liczby od 1 do 100 włącznie razem z informacją czy liczba jest parzysta czy nieparzysta.

# for liczba in range(1, 101):
#     if liczba % 2 == 0:
#         print(f"{liczba=} jest parzysta")
#     else:
#         print(f"{liczba=} jest nieparzysta")

# odwrócony warunek logiczny:
# for liczba in range(1, 101):
#     if liczba % 2:
#         print(f"{liczba=} jest nieparzysta")
#     else:
#         print(f"{liczba=} jest parzysta")

#### ZADANIE 8

# Napisz symulator lokaty Symulator ma przyjmować zmienne:
# - kwotę lokaty
# - oprocentowanie w skali roku
# - ilość miesięcy na jaką zakładamy lokatę
# Symulator ma dla każdego miesiąca lokaty wypisać który to miesiąc
# oraz ile mamy aktualnie zgromadzone po doliczeniu odsetek.
# Zakładamy kapitalizację odsetek co miesiąc.

# money = 100_000
# procent_rok = 6
# miesiace = 18

# p_miesiac = procent_rok / 100 / 12

# saldo = money
# for m in range(miesiace):
#     odsetki = p_miesiac * saldo
#     saldo = saldo + odsetki
#     # saldo += odsetki
#     print(f"Po miesiącu {m+1} {saldo=}")



## continue i break

# continue - przechodzi do kolejnej iteracji
# for i in range(20):
#     print(f"Przed ifem: {i=}")
#     if i < 10:
#         continue
#     print(f"Po ifie: {i=}")


# break - kończy całą pętlę
# for i in range(20):
#     print(f"Przed ifem: {i=}")
#     if i == 10:
#         break
#     print(f"Po ifie: {i=}")



#### ZADANIE 9

# Wypisz wynik dzielenia 1/x gdzie x to kolejne liczby od -10 do 10.
# Zrób tak, aby zapobiec dzieleniu przez 0