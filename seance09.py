# seance09.py - Compréhensions, tri, enumerate, zip

resultats = [
    {"nom": "Connexion valide", "module": "Authentification", "statut": "pass", "duree_secondes": 2.4},
    {"nom": "Mot de passe erroné", "module": "Authentification", "statut": "pass", "duree_secondes": 1.9},
    {"nom": "Ajout au panier", "module": "Panier", "statut": "fail", "duree_secondes": 3.1},
    {"nom": "Paiement par carte", "module": "Paiement", "statut": "pass", "duree_secondes": 4.8},
    {"nom": "Recherche de produit", "module": "Recherche", "statut": "fail", "duree_secondes": 2.2},
    {"nom": "Déconnexion", "module": "Authentification", "statut": "pass", "duree_secondes": 0.8},
]

# 1. Boucle classique, puis la même chose avec une compréhension
noms_echecs_boucle = []
for test in resultats:
    if test["statut"] == "fail":
        noms_echecs_boucle.append(test["nom"])

noms_echecs = [test["nom"] for test in resultats if test["statut"] == "fail"]
print("Échecs :", noms_echecs)
print("Même résultat :", noms_echecs == noms_echecs_boucle)

# 2. Transformer et calculer
durees = [test["duree_secondes"] for test in resultats]
print("Durées :", durees)
print("Total :", round(sum(durees), 1), "s")
print("Plus longue :", max(durees), "s")

# 3. Compréhension de dictionnaire : nom -> durée
duree_par_test = {test["nom"]: test["duree_secondes"] for test in resultats}
print(duree_par_test)

# 4. Tri avec lambda : les 3 tests les plus lents
plus_lents = sorted(resultats, key=lambda test: test["duree_secondes"], reverse=True)
for test in plus_lents[:3]:
    print(f"{test['nom']} : {test['duree_secondes']} s")

# 5. enumerate : numéroter
for numero, test in enumerate(resultats, start=1):
    print(f"{numero}. {test['nom']} [{test['statut']}]")

# 6. zip : parcourir deux listes en parallèle
noms = ["Connexion", "Panier", "Paiement"]
statuts = ["pass", "fail", "pass"]
for nom, statut in zip(noms, statuts):
    print(nom, "->", statut)

# 7. any / all
print("Au moins un échec :", any(test["statut"] == "fail" for test in resultats))
print("Tous réussis :", all(test["statut"] == "pass" for test in resultats))