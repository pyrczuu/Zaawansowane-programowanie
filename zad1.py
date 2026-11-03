import re


def is_palindrome(text: str) -> bool:
    words = re.findall(r'\b\w+\b', text.lower())
    combined = "".join(words)
    return combined == combined[::-1]
