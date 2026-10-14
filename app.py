from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
# Création de l'application NetWatch
app = Flask(__name__)
app.config["SECRET_KEY"] = "netwatch-local-development-key"


# Liste des équipements de notre réseau de démonstration
equipements = [
    {
        "nom": "Serveur principal",
        "adresse_ip": "192.168.1.10",
        "type": "Serveur",
        "statut": "En ligne"
    },
    {
        "nom": "Routeur central",
        "adresse_ip": "192.168.1.1",
        "type": "Routeur",
        "statut": "En ligne"
    },
    {
        "nom": "Switch étage 1",
        "adresse_ip": "192.168.1.20",
        "type": "Commutateur",
        "statut": "En ligne"
    },
    {
        "nom": "Serveur de sauvegarde",
        "adresse_ip": "192.168.1.30",
        "type": "Serveur",
        "statut": "Hors ligne"
    }
]
# Liste temporaire des incidents signalés
incidents = []

# Page d'accueil : tableau de bord
@app.route("/")
def accueil():
    total = len(equipements)

    en_ligne = sum(
        1 for equipement in equipements
        if equipement["statut"] == "En ligne"
    )

    hors_ligne = total - en_ligne

    disponibilite = round((en_ligne / total) * 100, 1) if total else 0

    return render_template(
        "index.html",
        equipements=equipements,
        total=total,
        en_ligne=en_ligne,
        hors_ligne=hors_ligne,
        disponibilite=disponibilite
    )

# Page À propos
@app.route("/about")
def about():
    return render_template("about.html")

# Page de signalement des incidents
@app.route("/report", methods=["GET", "POST"])
def report():

    # Si le formulaire est envoyé
    if request.method == "POST":

        # Récupérer les informations du formulaire
        equipement = request.form.get("equipment", "").strip()
        description = request.form.get("description", "").strip()

        # Vérifier que les champs sont remplis
        if not equipement or not description:
            flash("Veuillez remplir tous les champs.", "error")
            return redirect(url_for("report"))

        # Enregistrer le signalement
        incidents.append({
            "equipement": equipement,
            "description": description,
            "date": datetime.now().strftime("%d/%m/%Y %H:%M")
        })

        # Confirmer l'enregistrement
        flash("Votre signalement a été enregistré avec succès.", "success")

        return redirect(url_for("report"))

    # Afficher le formulaire
    return render_template("report.html")

 
# Démarrage du serveur en mode local
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)