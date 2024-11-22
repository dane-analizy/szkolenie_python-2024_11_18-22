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
    return render_template("temp_parametry.html", imie=ziomus)

if __name__ == "__main__":
    app.run(debug=True)
