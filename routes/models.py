from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy() # créer l'objet pour la database

#DB pour les utilisateurs
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

#DB pour stocker toutes les taches
#   une tache appartient a un seul utilisateur
#   un utilisateur peut avoir plusieurs taches
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.String(124), default=datetime.today().strftime("%d %B %Y"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("Users")

    def __repr__(self):
        return '<task %r>' % self.id