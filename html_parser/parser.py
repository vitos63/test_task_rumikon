from re import sub, findall
from collections import Counter
from typing import Dict


def top_10_words_in_html(file_path: str) -> Dict[str, int]:
    with open(file_path, encoding="utf-8") as file:
        file = sub(r"<[^>]+>", "", file.read())
    
    words = findall(r'[a-zA-Zа-яА-Я]{3,}', file)
    words_dict = Counter(word.lower() for word in words)
    
    result = {word:count for word,count in words_dict.most_common(10)}
    return result
