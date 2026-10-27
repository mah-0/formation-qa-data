# api_client.py - Appels à l'API JSONPlaceholder

import requests

URL_BASE = "https://jsonplaceholder.typicode.com"
DELAI_MAX = 10  # secondes


def obtenir_post(id_post):
    return requests.get(f"{URL_BASE}/posts/{id_post}", timeout=DELAI_MAX)


def obtenir_posts(id_utilisateur=None):
    parametres = {}
    if id_utilisateur is not None:
        parametres["userId"] = id_utilisateur
    return requests.get(f"{URL_BASE}/posts", params=parametres, timeout=DELAI_MAX)


def creer_post(titre, contenu, id_utilisateur):
    corps = {"title": titre, "body": contenu, "userId": id_utilisateur}
    return requests.post(f"{URL_BASE}/posts", json=corps, timeout=DELAI_MAX)


def obtenir_utilisateur(id_utilisateur):
    return requests.get(f"{URL_BASE}/users/{id_utilisateur}", timeout=DELAI_MAX)

def obtenir_utilisateurs():
    return requests.get(f"{URL_BASE}/users", timeout=DELAI_MAX)


def obtenir_commentaires(id_post):
    return requests.get(f"{URL_BASE}/posts/{id_post}/comments", timeout=DELAI_MAX)


def modifier_post(id_post, titre):
    corps = {"id": id_post, "title": titre, "body": "Contenu modifié", "userId": 1}
    return requests.put(f"{URL_BASE}/posts/{id_post}", json=corps, timeout=DELAI_MAX)


def supprimer_post(id_post):
    return requests.delete(f"{URL_BASE}/posts/{id_post}", timeout=DELAI_MAX)