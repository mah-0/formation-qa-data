# test_ui_connexion.py - Tests de saucedemo.com
import pytest
pytestmark = pytest.mark.ui

import pytest
from playwright.sync_api import Page, expect

URL = "https://www.saucedemo.com"


def se_connecter(page: Page, utilisateur, mot_de_passe):
    """Ouvre la page de connexion et soumet le formulaire."""
    page.goto(URL)
    page.get_by_placeholder("Username").fill(utilisateur)
    page.get_by_placeholder("Password").fill(mot_de_passe)
    page.get_by_role("button", name="Login").click()


def test_connexion_valide(page: Page):
    se_connecter(page, "standard_user", "secret_sauce")
    expect(page).to_have_url(f"{URL}/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")
    expect(page.locator(".inventory_item")).to_have_count(6)


@pytest.mark.parametrize(
    "utilisateur, mot_de_passe, message",
    [
        ("standard_user", "mauvais_mdp", "do not match"),
        ("utilisateur_inconnu", "secret_sauce", "do not match"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
    ],
)
def test_connexion_invalide(page: Page, utilisateur, mot_de_passe, message):
    se_connecter(page, utilisateur, mot_de_passe)
    erreur = page.locator("[data-test='error']")
    expect(erreur).to_be_visible()
    expect(erreur).to_contain_text(message)
    expect(page).not_to_have_url(f"{URL}/inventory.html")


def test_utilisateur_bloque(page: Page):
    se_connecter(page, "locked_out_user", "secret_sauce")
    expect(page.locator("[data-test='error']")).to_contain_text("locked out")




def test_ajout_au_panier(page_connectee: Page):
    page_connectee.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    expect(page_connectee.locator(".shopping_cart_badge")).to_have_text("1")
    expect(page_connectee.locator("[data-test='remove-sauce-labs-backpack']")).to_be_visible()

def test_panier_avec_deux_produits(page_connectee: Page):
    page_connectee.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    page_connectee.locator("[data-test='add-to-cart-sauce-labs-bike-light']").click()
    expect(page_connectee.locator(".shopping_cart_badge")).to_have_text("2")
    page_connectee.locator("[data-test='shopping-cart-link']").click()
    expect(page_connectee).to_have_url(f"{URL}/cart.html")
    expect(page_connectee.locator(".cart_item")).to_have_count(2)


def test_deconnexion(page_connectee: Page):
    page_connectee.get_by_role("button", name="Open Menu").click()
    page_connectee.locator("#logout_sidebar_link").click()
    expect(page_connectee.get_by_role("button", name="Login")).to_be_visible()
    expect(page_connectee).to_have_url(f"{URL}/")