# pakiet Flask
# pip install Flask

from flask import Flask, render_template

app = Flask("nasza apka")


@app.route("/")
def strona_glowna():
    return "jestem stroną główną"


@app.route("/templatka1")
def templatka1():
    return render_template("template_1.html")


@app.route("/templatka2")
def templatka2():
    return render_template("template_2.html")


@app.route("/templatka3")
def templatka3():
    return render_template("template_3.html")


@app.route("/temp_param")
@app.route("/temp_param/<ziomus>")
def templatka_parametry(ziomus=None):
    if not ziomus:
        ziomus = "Jasio"
    return render_template("temp_parametry.html", imie=ziomus, nazwisko="stałe nazisko")

@app.route("/tabela")
def tabela():
    kursy = [
        {"data": "data1", "waluta": "waluta1", "kurs": 1},
        {"data": "data2", "waluta": "waluta2", "kurs": 2},
        {"data": "data3", "waluta": "waluta3", "kurs": 3},
        {"data": "data4", "waluta": "waluta4", "kurs": 4},
        {"data": "data5", "waluta": "waluta5", "kurs": 5},
    ]
    return render_template("tabelka.html", notowania=kursy, current_waluta="EUR")


if __name__ == "__main__":
    app.run(debug=True)
