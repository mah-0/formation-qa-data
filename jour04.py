# jour04.py - Programme principal

from lecteur_json import charger_campagne, sauvegarder_rapport

nom, resultats = charger_campagne("resultats.json")

if len(resultats) > 0:
    print("Campagne :", nom)
    for resultat in resultats:
        print(resultat)
    sauvegarder_rapport("rapport.json", nom, resultats)
    print("Rapport enregistré dans rapport.json")