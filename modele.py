# modele.py - Une classe pour représenter un résultat de test


class ResultatTest:
    """Représente le résultat d'un test automatisé."""

    def __init__(self, nom, module, statut, duree_secondes):
        self.nom = nom
        self.module = module
        self.statut = statut.strip().lower()
        self.duree_secondes = duree_secondes

    def est_reussi(self):
        return self.statut == "pass"

    def est_en_echec(self):
        return self.statut == "fail"

    def __str__(self):
        return f"[{self.statut.upper()}] {self.nom} ({self.module}, {self.duree_secondes} s)"