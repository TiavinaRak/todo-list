from flask import Flask, render_template, url_for

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/inscription")
def inscription():
    return render_template("inscription.html")

@app.route("/connexion")
def connexion():
    return render_template("task.html")


if __name__ == "__main__":
    app.run(debug=True)