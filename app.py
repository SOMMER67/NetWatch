"""
NetWatch - Application Web de Supervision Réseau
Mini-projet Cloud Computing - AWS EC2 & Docker
"""

from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'netwatch-cloud-security-secret-key-2026'

# Données d'équipements surveillés (simulées)
DEVICES = [
    {
        "id": "dev-01",
        "name": "Routeur Gateway Principal",
        "type": "Router",
        "ip": "192.168.1.1",
        "status": "online",
        "ping": "2 ms",
        "uptime": "42j 14h",
        "traffic": "340 Mbps"
    },
    {
        "id": "dev-02",
        "name": "Switch Core 24P PoE+",
        "type": "Switch",
        "ip": "192.168.1.2",
        "status": "online",
        "ping": "1 ms",
        "uptime": "42j 12h",
        "traffic": "820 Mbps"
    },
    {
        "id": "dev-03",
        "name": "Passerelle Cloud AWS VPC",
        "type": "Gateway",
        "ip": "10.0.0.1",
        "status": "online",
        "ping": "11 ms",
        "uptime": "128j 06h",
        "traffic": "512 Mbps"
    },
    {
        "id": "dev-04",
        "name": "Instance Serveur Web EC2",
        "type": "Server",
        "ip": "13.53.48.105",
        "status": "online",
        "ping": "3 ms",
        "uptime": "18j 02h",
        "traffic": "145 Mbps"
    },
    {
        "id": "dev-05",
        "name": "Pare-Feu Edge / Firewall",
        "type": "Firewall",
        "ip": "192.168.1.254",
        "status": "online",
        "ping": "4 ms",
        "uptime": "42j 14h",
        "traffic": "980 Mbps"
    },
    {
        "id": "dev-06",
        "name": "Serveur DNS Résolveur",
        "type": "DNS Server",
        "ip": "1.1.1.1",
        "status": "online",
        "ping": "7 ms",
        "uptime": "210j 18h",
        "traffic": "25 Mbps"
    }
]

# Liste en mémoire des rapports d'incidents
REPORTS = [
    {
        "id": 1,
        "title": "Vérification des ports de sécurité AWS",
        "device": "Instance Serveur Web EC2 (13.53.48.105)",
        "category": "Sécurité",
        "severity": "Moyenne",
        "reporter": "Konaté Idrissa (SOMMER67)",
        "date": "2026-10-18 14:30",
        "description": "Ajout de la règle entrante TCP/80 dans le groupe de sécurité pour exposer le conteneur NetWatch au public.",
        "status": "Résolu"
    },
    {
        "id": 2,
        "title": "Optimisation du temps de réponse du Switch",
        "device": "Switch Core 24P PoE+ (192.168.1.2)",
        "category": "Performance",
        "severity": "Faible",
        "reporter": "Touré Ibrahim Hermann Junior (varanjfhueijd)",
        "date": "2026-10-19 09:15",
        "description": "Vérification du firmware et optimisation des buffers VLAN. Aucune perte de paquets constatée.",
        "status": "Résolu"
    }
]


@app.context_processor
def inject_global_data():
    return {
        "current_year": datetime.now().year,
        "app_version": "v1.0",
        "public_ip": "13.53.48.105",
        "docker_image": "sommer369/netwatch:v1",
        "github_repo": "https://github.com/SOMMER67/NetWatch"
    }


@app.route("/")
def dashboard():
    """Page d'accueil : Tableau de bord de supervision réseau."""
    total_devices = len(DEVICES)
    online_devices = sum(1 for d in DEVICES if d['status'] == 'online')
    uptime_avg = "99.98%"
    total_bandwidth = "2.82 Gbps"
    recent_reports = REPORTS[:4]
    
    return render_template(
        "dashboard.html",
        devices=DEVICES,
        total_devices=total_devices,
        online_devices=online_devices,
        uptime_avg=uptime_avg,
        total_bandwidth=total_bandwidth,
        recent_reports=recent_reports
    )


@app.route("/report", methods=["GET", "POST"])
def create_report():
    """Formulaire de soumission d'un rapport ou incident."""
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        device = request.form.get("device", "").strip()
        category = request.form.get("category", "Autre").strip()
        severity = request.form.get("severity", "Faible").strip()
        reporter = request.form.get("reporter", "").strip()
        description = request.form.get("description", "").strip()

        if not title or not description or not reporter:
            flash("Veuillez renseigner tous les champs obligatoires (Titre, Déclarant, Description).", "error")
            return render_template("report.html", devices=DEVICES, form=request.form)

        new_report = {
            "id": len(REPORTS) + 1,
            "title": title,
            "device": device,
            "category": category,
            "severity": severity,
            "reporter": reporter,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "description": description,
            "status": "En cours"
        }
        REPORTS.insert(0, new_report)
        flash("Rapport soumis avec succès ! Il a été intégré au tableau de bord.", "success")
        return redirect(url_for("reports_list"))

    return render_template("report.html", devices=DEVICES, form={})


@app.route("/reports")
def reports_list():
    """Liste complète des rapports enregistrés."""
    return render_template("reports_list.html", reports=REPORTS)


@app.route("/api/devices")
def api_devices():
    """API JSON retournant la liste des équipements et métriques."""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "total_nodes": len(DEVICES),
        "devices": DEVICES
    })


@app.route("/about")
def about():
    """Page d'informations sur le projet et l'équipe."""
    return render_template("about.html")


if __name__ == "__main__":
    # Démarre l'application sur toutes les interfaces pour Docker
    app.run(host="0.0.0.0", port=5000, debug=True)
