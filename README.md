# 📝 Todo-list – Application Web Flask

Application web de gestion de tâches développée avec Flask permettant à chaque utilisateur de gérer ses propres tâches après authentification.

---

## 🚀 Fonctionnalités
- Inscription et connexion des utilisateurs
- Gestion de tâches personnelles
- Interface simple et intuitive
- Données persistées avec une base SQLite

---

## 🛠 Technologies utilisées
- Backend : Python, Flask
- Frontend : HTML, CSS
- Base de données : SQLite
- Outils : Git, Virtual Environment (venv)

---

## 📦 Installation et exécution

### Cloner le dépôt
git clone https://github.com/TiavinaRak/todo-list.git  
cd todo-list

### Créer et activer un environnement virtuel
python -m venv venv

Activation :
source venv/bin/activate      (Linux / macOS)  
venv\\Scripts\\activate       (Windows)

### Installer les dépendances
pip install -r requirements.txt

### Lancer l’application
flask run

Puis ouvrir le navigateur à l’adresse :  
http://127.0.0.1:5000

---

## 🖼 Aperçu de l’interface

### 🔐 Authentification
![Connexion](images/connexion.png)  
![Inscription](images/inscription.png)

### 🏠 Page principale
![Accueil](images/home.png)

---

## 📈 Améliorations prévues
- Modification et suppression des tâches
- Historique des tâches supprimées
- Mise à jour des informations utilisateur
- Ajout et gestion des tâches sans rechargement de la page
- Amélioration de la sécurité et de la validation des formulaires
