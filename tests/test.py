from src import zad1, zad2, zad3, zad4, zad5, zad6, zad7
import pytest

def test_is_palindrome():
    assert zad1.is_palindrome("kajak") == True
    assert zad1.is_palindrome("Kobyła ma mały bok") == True
    assert zad1.is_palindrome("python") == False
    assert zad1.is_palindrome("") == True
    assert zad1.is_palindrome("A") == True

def test_fibonacci():
    assert zad2.fibonacci(0) == 1
    assert zad2.fibonacci(1) == 1
    assert zad2.fibonacci(5) == 5
    assert zad2.fibonacci(10) == 55
    with pytest.raises(ValueError):
        zad2.fibonacci(-1)
