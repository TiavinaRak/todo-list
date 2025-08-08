from flask import Flask, render_template, url_for, request, redirect
from routes.models import db, Users, Task
from datetime import datetime
import locale

# mettre la langue des dates en FR
locale.setlocale(locale.LC_TIME, 'fr_FR')

# créer l'application
app = Flask(__name__)

# spécifier le type de DB utiliser avec son nom et le chemin
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Database.db"
db.init_app(app) # initialiser la DB

with app.app_context():
    db.create_all() # créer toutes les tables

# afficher la page d'acceuil
@app.route("/")
def index():
    return render_template("index.html")

# fonction appeler lors de l'inscription d'un utilisateur
#   si POST: crée un nouvel utilisateur
#   sinon : affiche la page d'inscription
#   ses informations sont envoyés a la DB Users
@app.route("/inscription", methods=["POST", "GET"])
def inscription():
    if request.method == "POST":
        if request.form["mot_de_passe"] == request.form["verification_mdp"]:
            # récupérer les infos entrer par l'utilisateur
            nom, em, pwd = request.form["nom"], request.form["email"], request.form["mot_de_passe"]
            # initialiser un nouvel utilisateur
            new_user = Users(name=nom, email=em, password=pwd)
            try:
                db.session.add(new_user) # ajouter l'utilisateur
                db.session.commit() # envoyer la requête
                return redirect("/") # retourner a la page de connexion
            except:
                return "there was an issue creating your account"
    return render_template("inscription.html")

# fonction appeler quand on essaie de se connecter
@app.route("/connexion", methods=['GET', 'POST'])
def connexion():
    users = Users.query.all() # récupérer tous les utilisateurs
    email, password = request.form["email"] ,request.form["password"]
    for user in users:
        # vérifier si les infos entrés par l'utilisateurs sont exacts
        if user.email == email and user.password == password:
            USER_CONNECTED["name"] = user.name
            USER_CONNECTED["id"] = user.id
            return redirect("/mes_taches") # appel la fonction qui redirige vers la page des taches
    return redirect("/")

# fonction permettant d'ajouter une nouvelle tache
@app.route("/ajouter_tache", methods=['GET', 'POST'])
def ajouter_tache():
    if request.form["tache"] == "":
        return redirect("/mes_taches")
    new_task = Task(content=request.form["tache"], user_id=USER_CONNECTED["id"],
                    date_created=datetime.today().strftime("%d %B"))
    try:
        db.session.add(new_task)
        db.session.commit()
        return redirect("/mes_taches")
    except:
        return "there was an issue creating your account"


@app.route("/mes_taches", methods=['GET', 'POST'])
def afficher_taches():
    tasks = Task.query.where(Task.user_id==USER_CONNECTED["id"]).all()
    return render_template("task.html", task_list=tasks,
                           username=USER_CONNECTED["name"],
                           today_date=datetime.today().strftime("%d %B %Y"))

@app.route("/deconnexion")
def deconnexion():
    USER_CONNECTED["name"] = ""
    USER_CONNECTED["id"] = 0
    return redirect("/")


if __name__ == "__main__":
    USER_CONNECTED = {
        "name" : "",
        "id" : 0
    }
    app.run(debug=True)