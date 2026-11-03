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

def test_count_vowels():
    assert zad3.count_vowels("Python") == 2
    assert zad3.count_vowels("AEIOUY") == 6
    assert zad3.count_vowels("bcd") == 0
    assert zad3.count_vowels("") == 0
    assert zad3.count_vowels("Python żółwia") == 4

def test_calculate_discount():
    assert zad4.calculate_discount(100, 0.2) == 80.0
    assert zad4.calculate_discount(50, 0) == 50.0
    assert zad4.calculate_discount(200, 1) == 0.0
    with pytest.raises(ValueError):
        zad4.calculate_discount(100, -1)
        zad4.calculate_discount(100, 1.5)

def test_flatten_list():
    assert zad5.flatten_list([1,2,3]) == [1,2,3]
    assert zad5.flatten_list([1, [2, 3], [4, [5]]]) == [1,2,3,4,5]
    assert zad5.flatten_list([]) == []
    assert zad5.flatten_list([[[1]]]) == [1]
    assert zad5.flatten_list([1, [2, [3, [4]]]]) == [1,2,3,4]


def test_word_frequencies():
    assert zad6.word_frequencies("To be or not to be") == {"to": 2, "be": 2, "or": 1, "not": 1}
    assert zad6.word_frequencies("Hello, hello!") == {"hello": 2}
    assert zad6.word_frequencies("") == {}
    assert zad6.word_frequencies("Python Python python") == {"python": 3}
    assert zad6.word_frequencies("Ala ma kota, a kot ma Ale.") == {"ala": 1, "ma": 2,
                                                                   "kota": 1, "a": 1, "kot": 1, "ale": 1}