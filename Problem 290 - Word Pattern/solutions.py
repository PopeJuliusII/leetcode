from itertools import zip_longest


def solution_1(pattern: str, s: str) -> bool:
    letter_word, word_letter = {}, {}
    for key, value in zip_longest(pattern, s.split(), fillvalue=None):
        if key is None or value is None or letter_word.get(key, value) != value or word_letter.get(value, key) != key:
            return False
        letter_word[key], word_letter[value] = value, key
    return True
