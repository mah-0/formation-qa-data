# jour01.py - Résultats de tests : compter, calculer, afficher

# 1. Une liste de dictionnaires : chaque dictionnaire représente un test
tests = [
    {"nom": "Connexion valide", "statut": "pass"},
    {"nom": "Connexion mot de passe erroné", "statut": "pass"},
    {"nom": "Ajout au panier", "statut": "fail"},
    {"nom": "Paiement par carte", "statut": "pass"},
    {"nom": "Recherche de produit", "statut": "fail"},
    {"nom": "Déconnexion", "statut": "pass"},
    
]


# 2. Une fonction qui compte les réussites et les échecs
def compter_resultats(liste_tests):
    reussites = 0
    echecs = 0
    for test in liste_tests:
        if test["statut"] == "pass":
            reussites = reussites + 1
        else:
            echecs = echecs + 1
    return reussites, echecs


# 3. Une fonction qui calcule le taux de réussite en pourcentage
def taux_reussite(liste_tests):
    reussites, echecs = compter_resultats(liste_tests)
    total = reussites + echecs
    if total == 0:
        return 0.0
    return round(reussites / total * 100, 1)


# 4. Une fonction qui affiche les noms des tests en échec
def afficher_echecs(liste_tests):
    print("Tests en échec :")
    for test in liste_tests:
        if test["statut"] == "fail":
            print("-", test["nom"])


# 5. Programme principal
reussites, echecs = compter_resultats(tests)
print("Réussites :", reussites)
print("Échecs :", echecs)
print("Taux de réussite :", taux_reussite(tests), "%")
afficher_echecs(tests)