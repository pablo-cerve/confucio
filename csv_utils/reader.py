import sys
sys.path.append('.')

import csv

from classes.word import Word
from classes.word_meaning import WordMeaning
from csv_utils.common import Common


class Reader:
    def __init__(self, book_number, lesson_number, lesson_extra=False):
        self.book_number = book_number
        self.lesson_number = lesson_number
        self.path = Common.book_lesson_path(self.book_number, lesson_number, lesson_extra)
        print(self.path)

    def generate_words(self):
        words = []
        with open(self.path) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for index, row in enumerate(reader):
                if index == 0:
                    assert(row == Common.FIRST_ROW)
                    continue
                word = self.__process_row(row, len(words) + 1)
                words.append(word)
        return words

    def __process_row(self, row, word_number):
        hanzi, pinyin, definition1, word_type1, definition2, word_type2, _, _ = row

        word_meanings = [WordMeaning(word_type1, definition1)]
        if len(definition2) > 0:
            word_meanings.append(WordMeaning(word_type2, definition2))

        return Word(pinyin, hanzi, definition1, word_meanings, word_number, self.lesson_number)
