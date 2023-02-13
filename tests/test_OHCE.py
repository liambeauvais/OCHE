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
    assert response[1] == "totot"
    assert response[2] == "Bien dit"

def test_hello():
    palindrome = Palindrome()
    """Quand on saisit une chaine alors <Bonjour> est envoyé avant toute réponse"""
    #QUAND on saisit un chaîne
    input = "toto"
    #ALORS <Bonjour> est envoyé avant toute réponse
    response = palindrome.mirror(input).split('\n')
    assert  "Bonjour" in response[0]

def test_goodbye():
    palindrome = Palindrome()
    """Quant on saisit une chaîne, alors <Au revoir> est envoyée en dernier"""
    #QUAND on saisit une chaîne
    input = "toto"
    #ALORS <Au revoir> est envoyé en dernier
    response = palindrome.mirror(input).split('\n')
    assert "Au revoir" in response[-1]

def test_language():
    """Etant donné un utilisateur parlant une langue, quand on rentre un palindrome,
     alors il est renvoyé, et le <BienDit> de cette langue est envoyé"""
    #ETANT donné un utilisateur parlant une langue
    french = Palindrome(locale_time="fr_FR")
    english = Palindrome(locale_time="en_US")
    #QUAND on rentre un palindrome
    palindrome = "totot"
    #ALORS il est renvoyé
    response_french = french.mirror(palindrome).split('\n')
    response_english = english.mirror(palindrome).split('\n')
    assert response_french[1] == "totot"
    assert response_english[1] == "totot"
    #ET le <BienDit> de cette langue est envoyé
    assert response_english[2] == "Well said"
    assert response_french[2] == "Bien dit"

    def test_language_hello():
        """Etant donné un utilisateur parlant une langue, quand on saisit une chaîne de caractère,
        alors <bonjour> de cette langue est renvoyé avant tout"""
        # ETANT donné un utilisateur parlant une langue
        french = Palindrome(locale_time="fr_FR")
        english = Palindrome(locale_time="en_US")
        #QUAND on saisit un chaîne de caractères
        input = "toto"
        #ALORS <bonjour> de cette langue est renvoyé avant tout
        response_french = french.mirror(palindrome).split('\n')
        response_english = english.mirror(palindrome).split('\n')
        assert "Bonjour" in response_french[0]
        assert "Hello" in response_english[0]


    def test_language_goodbye():
        """Etant donné un utilisateur parlant une langue, quand on saisit une chaîne de caractère,
        alors <auRevoir> dans cette langue est renvoyé en dernier"""
        # ETANT donné un utilisateur parlant une langue
        french = Palindrome(locale_time="fr_FR")
        english = Palindrome(locale_time="en_US")
        # ALORS <auRevoir> de cette langue est renvoyé en dernier
        response_french = french.mirror(palindrome).split('\n')
        response_english = english.mirror(palindrome).split('\n')
        assert "Au revoir" in response_french[-1]
        assert "Goodbye" in response_english[-1]
