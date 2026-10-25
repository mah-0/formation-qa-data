# test_lecteur_json.py - Tests de la lecture JSON

import json

from lecteur_json import charger_campagne


def test_charger_campagne(tmp_path):
    contenu = {
        "campagne": "Test",
        "tests": [
            {"nom": "A", "module": "Auth", "statut": "pass", "duree_secondes": 1.0}
        ],
    }
    fichier = tmp_path / "mini.json"
    fichier.write_text(json.dumps(contenu), encoding="utf-8")

    nom, resultats = charger_campagne(str(fichier))

    assert nom == "Test"
    assert len(resultats) == 1
    assert resultats[0].nom == "A"


def test_charger_campagne_fichier_absent():
    nom, resultats = charger_campagne("n_existe_pas.json")
    assert nom is None
    assert resultats == []