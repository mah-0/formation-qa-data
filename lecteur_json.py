# lecteur_json.py - Lire et écrire des fichiers JSON

import json

from modele import ResultatTest


def charger_campagne(chemin_fichier):
    """Lit un fichier JSON et retourne (nom_campagne, liste de ResultatTest)."""
    try:
        with open(chemin_fichier, encoding="utf-8") as fichier:
            donnees = json.load(fichier)
    except FileNotFoundError:
        print("Erreur : fichier introuvable :", chemin_fichier)
        return None, []
    except json.JSONDecodeError as erreur:
        print("Erreur : JSON invalide :", erreur)
        return None, []

    resultats = []
    for element in donnees["tests"]:
        resultat = ResultatTest(
            nom=element["nom"],
            module=element["module"],
            statut=element["statut"],
            duree_secondes=element["duree_secondes"],
        )
        resultats.append(resultat)
    return donnees["campagne"], resultats


def sauvegarder_rapport(chemin_fichier, nom_campagne, resultats):
    """Écrit un petit rapport JSON avec les totaux."""
    reussis = 0
    echecs = []
    for resultat in resultats:
        if resultat.est_reussi():
            reussis = reussis + 1
        elif resultat.est_en_echec():
            echecs.append(resultat.nom)

    rapport = {
        "campagne": nom_campagne,
        "total": len(resultats),
        "reussis": reussis,
        "echecs": echecs,
    }
    with open(chemin_fichier, "w", encoding="utf-8") as fichier:
        json.dump(rapport, fichier, indent=2, ensure_ascii=False)