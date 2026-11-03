def count_vowels(text: str) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
