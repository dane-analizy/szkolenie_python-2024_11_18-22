zmienna_x = 123


def hello(imie):
    print(f"Witaj {imie}!")



if __name__ == "__main__":
    print("uruchomiłeś mnie (jestem modul_dwa.py)")

    print(__name__)  # __main__

    hello("Janek")
    print(f"jestem na końcu modul_dwa.py, a zmienna_x = {zmienna_x}")
