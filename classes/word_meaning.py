
from word_type import WordType


class WordMeaning:
    def __init__(self, word_type_key, word_meaning_str, book_number=None):
        self.word_type = WordType(word_type_key, book_number)
        self.word_meaning_str = word_meaning_str
