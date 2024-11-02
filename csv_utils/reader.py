import sys
sys.path.append('.')

import csv

from classes.word import Word
from classes.word_meaning import WordMeaning
from csv_utils.common import Common


class Reader:
    def __init__(self, path, lesson_number=100):
        self.path = path
        self.lesson_number = lesson_number

    def generate_words(self):
        words = []
        with open(self.path) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for index, row in enumerate(reader):
                if index == 0:
                    if self.lesson_number == 'hsk5':
                        assert(row == Common.FIRST_ROW_HSK5)
                    elif self.lesson_number == 'hsk4':
                        assert(row == Common.FIRST_ROW_HSK4)
                    elif self.lesson_number == 'hsk3':
                        assert(row == Common.FIRST_ROW_HSK3)
                    else:
                        print(row)
                        print(Common.FIRST_ROW_LESSON)
                        assert(row == Common.FIRST_ROW_LESSON)
                    continue
                word = self.__process_row(row, len(words) + 1)
                if word is not None:
                    words.append(word)
        return words

    def __process_row(self, row, word_number):
        row_length = len(row)
        lesson_number = None
        if self.lesson_number == 'hsk5':
            assert(row_length == 9)
            hanzi, pinyin, word_type1, definition1, word_type2, definition2, lesson_number, word_number, featured = row
            if hanzi == "":
                return
            is_featured = len(featured) > 0
            lesson_number = str(lesson_number)
        elif self.lesson_number == 'hsk4':
            assert(row_length == 9)
            hanzi, pinyin, definition1, word_type1, definition2, word_type2, lesson_number, word_number, featured = row
            is_featured = len(featured) > 0
            lesson_number = str(lesson_number)
        elif self.lesson_number == 'hsk3':
            assert(row_length == 11)
            hanzi, pinyin, definition1, word_type1, definition2, word_type2, _, _, _, _, _ = row
        else:
            assert(row_length == 8)
            hanzi, pinyin, definition1, word_type1, definition2, word_type2, _, _ = row

        word_meanings = [WordMeaning(word_type1, definition1)]
        if len(definition2) > 0:
            word_meanings.append(WordMeaning(word_type2, definition2))

        return Word(pinyin, hanzi, definition1, word_meanings, word_number, lesson_number, is_featured)
