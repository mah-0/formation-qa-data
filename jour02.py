# jour02.py - Lire un fichier CSV de résultats de tests

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
        statut = test["statut"]
        if statut in compteurs:
            compteurs[statut] = compteurs[statut] + 1
        else:
            compteurs[statut] = 1
    return compteurs


def duree_moyenne(resultats):
    """Retourne la durée moyenne des tests, arrondie à 1 décimale."""
    if len(resultats) == 0:
        return 0.0
    total = 0.0
    for test in resultats:
        total = total + test["duree_secondes"]
    return round(total / len(resultats), 1)


def echecs_par_module(resultats):
    """Retourne le nombre de tests en échec pour chaque module."""
    modules = {}
    for test in resultats:
        if test["statut"] == "fail":
            module = test["module"]
            modules[module] = modules.get(module, 0) + 1
    return modules


# Programme principal
resultats = lire_resultats("resultats.csv")

if len(resultats) > 0:
    print(f"Nombre de tests : {len(resultats)}")
    print("Par statut :", compter_par_statut(resultats))
    print(f"Durée moyenne : {duree_moyenne(resultats)} s")
    print("Échecs par module :", echecs_par_module(resultats))