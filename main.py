from flask import Flask, url_for, redirect, render_template


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/ml")
def ml():
    return render_template("ml.html")

@app.route("/games")
def games():
    return render_template("games.html")


if __name__ == "__main__":
    app.run(debug=True)
