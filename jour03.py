# jour03.py - Programme principal qui utilise le module analyse

from analyse import (
    lire_resultats,
    compter_par_statut,
    taux_reussite,
    duree_moyenne,
    echecs_par_module,
)

resultats = lire_resultats("resultats.csv")

if len(resultats) > 0:
    print(f"Nombre de tests : {len(resultats)}")
    print("Par statut :", compter_par_statut(resultats))
    print(f"Taux de réussite : {taux_reussite(resultats)} %")
    print(f"Durée moyenne : {duree_moyenne(resultats)} s")
    print("Échecs par module :", echecs_par_module(resultats))