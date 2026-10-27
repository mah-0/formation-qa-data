# test_api_posts.py - Tests automatisés de l'API JSONPlaceholder

import pytest

from api_client import (
    obtenir_post,
    obtenir_posts,
    creer_post,
    obtenir_utilisateur,
    obtenir_utilisateurs,
    obtenir_commentaires,
    modifier_post,
    supprimer_post,
)


def test_obtenir_post_existant():
    reponse = obtenir_post(1)
    assert reponse.status_code == 200
    donnees = reponse.json()
    assert donnees["id"] == 1
    assert donnees["userId"] == 1


def test_post_a_les_bons_champs():
    donnees = obtenir_post(1).json()
    for cle in ["userId", "id", "title", "body"]:
        assert cle in donnees
    assert isinstance(donnees["title"], str)
    assert donnees["title"] != ""


def test_post_inexistant_retourne_404():
    reponse = obtenir_post(9999)
    assert reponse.status_code == 404


def test_liste_des_posts():
    reponse = obtenir_posts()
    assert reponse.status_code == 200
    assert len(reponse.json()) == 100


def test_filtrer_posts_par_utilisateur():
    posts = obtenir_posts(id_utilisateur=1).json()
    assert len(posts) > 0
    for post in posts:
        assert post["userId"] == 1


def test_creer_post():
    reponse = creer_post("Mon titre", "Mon contenu", 1)
    assert reponse.status_code == 201
    donnees = reponse.json()
    assert donnees["title"] == "Mon titre"
    assert donnees["userId"] == 1
    assert "id" in donnees


def test_type_de_contenu_json():
    reponse = obtenir_post(1)
    assert "application/json" in reponse.headers["Content-Type"]


def test_temps_de_reponse():
    reponse = obtenir_post(1)
    assert reponse.elapsed.total_seconds() < 2.0


def test_utilisateur_a_un_courriel_valide():
    donnees = obtenir_utilisateur(1).json()
    assert "@" in donnees["email"]



def test_liste_des_utilisateurs():
    reponse = obtenir_utilisateurs()
    assert reponse.status_code == 200
    utilisateurs = reponse.json()
    assert isinstance(utilisateurs, list)
    assert len(utilisateurs) > 0
    for utilisateur in utilisateurs:
        assert "@" in utilisateur["email"]

def test_commentaires_du_post_1():
    reponse = obtenir_commentaires(1)
    assert reponse.status_code == 200
    commentaires = reponse.json()
    assert len(commentaires) > 0
    for commentaire in commentaires:
        assert commentaire["postId"] == 1
        assert "@" in commentaire["email"]        


def test_modifier_post():
    reponse = modifier_post(1, "Nouveau titre")
    assert reponse.status_code == 200
    assert reponse.json()["title"] == "Nouveau titre"


def test_supprimer_post():
    reponse = supprimer_post(1)
    assert reponse.status_code == 200


@pytest.mark.parametrize("id_post", [0, 101, 9999])
def test_posts_inexistants(id_post):
    reponse = obtenir_post(id_post)
    assert reponse.status_code == 404    

@pytest.mark.parametrize(
    "id_post, statut_attendu",
    [(1, 200), (50, 200), (100, 200), (101, 404)],
)
def test_statut_selon_identifiant(id_post, statut_attendu):
    reponse = obtenir_post(id_post)
    assert reponse.status_code == statut_attendu    