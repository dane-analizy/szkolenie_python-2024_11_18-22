# pakiet Flask
# pip install Flask

from flask import Flask

app = Flask("nasza apka")


@app.route("/")
def strona_glowna():
    return "jestem stroną główną"


@app.route("/kontakt")
def kontakt():
    return "jestem stroną z kontaktem"


@app.route("/dodaj/<a>/<b>")
def dodawanie(a, b):
    suma = float(a) + float(b)
    return f"Wynik dodawania {a} + {b} = {suma}"


@app.route("/pomnoz/<a>/<b>")
def mnozenie(a, b):
    suma = float(a) * float(b)
    return f"Wynik mnożenia {a} * {b} = {suma}"


@app.route("/witaj/<imie>")
def witaj(imie):
    return f"<h1>Witaj {imie}!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
