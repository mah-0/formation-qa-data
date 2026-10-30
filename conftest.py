# conftest.py - Fixtures partagées par tous les tests

import time

import pytest
from playwright.sync_api import Page

URL_SAUCEDEMO = "https://www.saucedemo.com"


@pytest.fixture
def tests_exemple():
    """4 résultats de tests aux valeurs connues, pour les tests d'analyse."""
    return [
        {"nom": "A", "module": "Auth", "statut": "pass", "duree_secondes": 2.0},
        {"nom": "B", "module": "Auth", "statut": "fail", "duree_secondes": 4.0},
        {"nom": "C", "module": "Panier", "statut": "pass", "duree_secondes": 3.0},
        {"nom": "D", "module": "Panier", "statut": "skip", "duree_secondes": 3.0},
    ]


@pytest.fixture
def page_connectee(page: Page):
    """Une page déjà connectée à saucedemo.com avec standard_user."""
    page.goto(URL_SAUCEDEMO)
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    return page


@pytest.fixture
def chrono():
    """Mesure et affiche la durée d'un test (démonstration de yield)."""
    debut = time.perf_counter()
    yield
    duree = time.perf_counter() - debut
    print(f"\nDurée du test : {duree:.2f} s")