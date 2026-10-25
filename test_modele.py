# test_modele.py - Tests de la classe ResultatTest

from modele import ResultatTest


def test_resultat_reussi():
    resultat = ResultatTest("Connexion", "Auth", "pass", 1.5)
    assert resultat.est_reussi() is True
    assert resultat.est_en_echec() is False


def test_statut_normalise():
    resultat = ResultatTest("Connexion", "Auth", " PASS ", 1.5)
    assert resultat.statut == "pass"


def test_affichage():
    resultat = ResultatTest("Connexion", "Auth", "fail", 1.5)
    assert str(resultat) == "[FAIL] Connexion (Auth, 1.5 s)"