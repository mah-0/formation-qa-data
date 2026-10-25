# test_analyse.py - Tests automatisés des fonctions d'analyse

from analyse import (
    compter_par_statut,
    taux_reussite,
    duree_moyenne,
    echecs_par_module,
    trouver_test_le_plus_lent,
)


def creer_tests_exemple():
    """Données de test : 4 tests avec des résultats connus à l'avance."""
    return [
        {"nom": "A", "module": "Auth", "statut": "pass", "duree_secondes": 2.0},
        {"nom": "B", "module": "Auth", "statut": "fail", "duree_secondes": 4.0},
        {"nom": "C", "module": "Panier", "statut": "pass", "duree_secondes": 3.0},
        {"nom": "D", "module": "Panier", "statut": "skip", "duree_secondes": 3.0},
    ]


def test_compter_par_statut():
    resultats = creer_tests_exemple()
    assert compter_par_statut(resultats) == {"pass": 2, "fail": 1, "skip": 1}


def test_taux_reussite():
    resultats = creer_tests_exemple()
    assert taux_reussite(resultats) == 50.0


def test_taux_reussite_liste_vide():
    assert taux_reussite([]) == 0.0


def test_duree_moyenne():
    resultats = creer_tests_exemple()
    assert duree_moyenne(resultats) == 3.0


def test_duree_moyenne_liste_vide():
    assert duree_moyenne([]) == 0.0


def test_echecs_par_module():
    resultats = creer_tests_exemple()
    assert echecs_par_module(resultats) == {"Auth": 1}


def test_taux_reussite_tout_pass():
    resultats = [
        {"nom": "A", "module": "Auth", "statut": "pass", "duree_secondes": 1.0},
        {"nom": "B", "module": "Panier", "statut": "pass", "duree_secondes": 2.0},
    ]
    assert taux_reussite(resultats) == 100.0   

def test_echecs_par_module_aucun_echec():
    resultats = [
        {"nom": "A", "module": "Auth", "statut": "pass", "duree_secondes": 1.0},
        {"nom": "B", "module": "Panier", "statut": "skip", "duree_secondes": 2.0},
    ]
    assert echecs_par_module(resultats) == {}

def test_trouver_test_le_plus_lent():
    assert trouver_test_le_plus_lent(creer_tests_exemple()) == "B"


def test_trouver_test_le_plus_lent_liste_vide():
    assert trouver_test_le_plus_lent([]) is None    


def test_statut_en_majuscules():
    resultats = [
        {"nom": "A", "module": "Auth", "statut": "PASS", "duree_secondes": 1.0},
    ]
    assert taux_reussite(resultats) == 100.0   