# jour05.py - Premiers appels à l'API

from api_client import obtenir_post, obtenir_posts, creer_post

reponse = obtenir_post(1)
print("Statut :", reponse.status_code)
print("Type de contenu :", reponse.headers["Content-Type"])
donnees = reponse.json()
print("Identifiant :", donnees["id"])
print("Auteur (userId) :", donnees["userId"])
print("Titre :", donnees["title"])

reponse = obtenir_posts()
print("Nombre de posts :", len(reponse.json()))

reponse = obtenir_posts(id_utilisateur=1)
print("Posts de l'utilisateur 1 :", len(reponse.json()))

reponse = obtenir_post(9999)
print("Post inexistant, statut :", reponse.status_code)

reponse = creer_post("Mon titre", "Mon contenu", 1)
print("Création, statut :", reponse.status_code)
print("Réponse :", reponse.json())