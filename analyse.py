# analyse.py - Fonctions d'analyse de résultats de tests

import csv


def lire_resultats(chemin_fichier):
    """Lit un fichier CSV et retourne une liste de dictionnaires."""
    resultats = []
    try:
        with open(chemin_fichier, newline="", encoding="utf-8") as fichier:
            lecteur = csv.DictReader(fichier)
            for ligne in lecteur:
                try:
                    ligne["duree_secondes"] = float(ligne["duree_secondes"])
                except ValueError:
                    print("Durée invalide pour le test :", ligne["nom"])
                    ligne["duree_secondes"] = 0.0
                resultats.append(ligne)
    except FileNotFoundError:
        print("Erreur : le fichier", chemin_fichier, "est introuvable.")
    return resultats


def compter_par_statut(resultats):
    """Retourne un dictionnaire comme {'pass': 5, 'fail': 2, 'skip': 1}."""
    compteurs = {}
    for test in resultats:
        statut = test["statut"].strip().lower()
        compteurs[statut] = compteurs.get(statut, 0) + 1
    return compteurs


def taux_reussite(resultats):
    """Pourcentage de tests 'pass' sur le total, arrondi à 1 décimale."""
    if len(resultats) == 0:
        return 0.0
    compteurs = compter_par_statut(resultats)
    reussites = compteurs.get("pass", 0)
    return round(reussites / len(resultats) * 100, 1)


def duree_moyenne(resultats):
    """Durée moyenne des tests, arrondie à 1 décimale."""
    if len(resultats) == 0:
        return 0.0
    total = 0.0
    for test in resultats:
        total = total + test["duree_secondes"]
    return round(total / len(resultats), 1)


def echecs_par_module(resultats):
    """Nombre de tests en échec pour chaque module."""
    modules = {}
    for test in resultats:
        if test["statut"] == "fail":
            module = test["module"]
            modules[module] = modules.get(module, 0) + 1
    return modules

def trouver_test_le_plus_lent(resultats):
    """Retourne le nom du test le plus long, ou None si la liste est vide."""
    if len(resultats) == 0:
        return None
    plus_lent = resultats[0]
    for test in resultats:
        if test["duree_secondes"] > plus_lent["duree_secondes"]:
            plus_lent = test
    return plus_lent["nom"]