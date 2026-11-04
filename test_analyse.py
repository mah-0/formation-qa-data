# test_analyse.py - Tests automatisés des fonctions d'analyse
import pytest

pytestmark = pytest.mark.unitaire

from analyse import (
    compter_par_statut,
    taux_reussite,
    duree_moyenne,
    echecs_par_module,
    trouver_test_le_plus_lent,
    modules_en_echec,
    classer_par_duree
)





def test_compter_par_statut(tests_exemple):
    assert compter_par_statut(tests_exemple) == {"pass": 2, "fail": 1, "skip": 1}


def test_taux_reussite(tests_exemple):
    assert taux_reussite(tests_exemple) == 50.0


def test_taux_reussite_liste_vide():
    assert taux_reussite([]) == 0.0


def test_duree_moyenne(tests_exemple):
     
    assert duree_moyenne(tests_exemple) == 3.0


def test_duree_moyenne_liste_vide():
    assert duree_moyenne([]) == 0.0


def test_echecs_par_module(tests_exemple):
     
    assert echecs_par_module(tests_exemple) == {"Auth": 1}


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

def test_trouver_test_le_plus_lent(tests_exemple):
    assert trouver_test_le_plus_lent(tests_exemple) == "B"


def test_trouver_test_le_plus_lent_liste_vide():
    assert trouver_test_le_plus_lent([]) is None    


def test_statut_en_majuscules():
    resultats = [
        {"nom": "A", "module": "Auth", "statut": "PASS", "duree_secondes": 1.0},
    ]
    assert taux_reussite(resultats) == 100.0   


def test_modules_en_echec():
    resultats = [
        {"nom": "A", "module": "Panier", "statut": "fail", "duree_secondes": 1.0},
        {"nom": "B", "module": "Auth", "statut": "fail", "duree_secondes": 1.0},
        {"nom": "C", "module": "Panier", "statut": "fail", "duree_secondes": 1.0},
        {"nom": "D", "module": "Paiement", "statut": "pass", "duree_secondes": 1.0},
    ]
    assert modules_en_echec(resultats) == ["Auth", "Panier"]


def test_modules_en_echec_aucun_echec():
    resultats = [
        {"nom": "A", "module": "Auth", "statut": "pass", "duree_secondes": 1.0},
    ]
    assert modules_en_echec(resultats) == []


def test_classer_par_duree():
    resultats = [
        {"nom": "A", "module": "X", "statut": "pass", "duree_secondes": 1.0},
        {"nom": "B", "module": "X", "statut": "pass", "duree_secondes": 5.0},
        {"nom": "C", "module": "X", "statut": "pass", "duree_secondes": 3.0},
    ]
    assert classer_par_duree(resultats) == ["B", "C", "A"]    