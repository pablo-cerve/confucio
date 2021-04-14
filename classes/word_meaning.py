
from classes.word_type import WordType


class WordMeaning:
    def __init__(self, word_type_key, word_meaning_str):
        self.word_type = WordType(word_type_key)
        self.word_meaning_str = word_meaning_str
