from src import zad1, zad2, zad3, zad4, zad5, zad6, zad7


def test_is_palindrome():
    assert zad1.is_palindrome("kajak") == True
    assert zad1.is_palindrome("Kobyła ma mały bok") == True
    assert zad1.is_palindrome("python") == False
    assert zad1.is_palindrome("") == True
    assert zad1.is_palindrome("A") == True

