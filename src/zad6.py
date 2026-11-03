import re
from collections import Counter

def word_frequencies(text: str) -> dict:
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)
