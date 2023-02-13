import pytest

from OHCE import Palindrome


def test_mirror():
    """Quant on saisit une chaîne alors celle-ci est renvoyée en mirroir"""
    palindrome = Palindrome()
    # QUAND on saisit un chaîne
    input = "toto"
    # ALORS celle-ci est renvoyée en mirroir
    response = palindrome.mirror(input).split('\n')
    assert response[1] == "otot"


def test_mirror_is_palindrome():
    palindrome = Palindrome()
    """Quand on saisit un palindrome alors celui-ci est renvoyé et <Bien dit> est envoyé ensuite"""
    # QUAND on saisit un palindrome
    input = "totot"
    # ALORS celui-ci est renvoyé
    response = palindrome.mirror(input).split('\n')
    print(response)
    assert response[1] == "totot"
    assert response[2] == "Bien dit"

def test_hello():
    palindrome = Palindrome()
    """Quand on saisit une chaine alors <Bonjour> est envoyé avant toute réponse"""
    #QUAND on saisit un chaîne
    input = "toto"
    #ALORS <Bonjour> est envoyé avant toute réponse
    response = palindrome.mirror(input).split('\n')
    assert response[0] == "Bonjour"

def test_goodbye():
    palindrome = Palindrome()
    """Quant on saisit une chaîne, alors <Au revoir> est envoyée en dernier"""
    #QUAND on saisit une chaîne
    input = "toto"
    #ALORS <Au revoir> est envoyé en dernier
    response = palindrome.mirror(input).split('\n')
    print(response)
    assert response[-1] == "Au revoir"