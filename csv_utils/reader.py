import sys
sys.path.append('.')

import csv

from classes.lesson import Lesson
from classes.word import Word
from classes.word_meaning import WordMeaning
from csv_utils.common import Common


class Reader:
    def __init__(self, lesson_number):
        self.lesson_number = lesson_number
        self.book_number = Lesson.book_number(lesson_number)
        self.path = Common.book_lesson_path(self.book_number, lesson_number)
        print(self.path)

    def generate_lesson(self):
        words = []
        with open(self.path) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for index, row in enumerate(reader):
                if index == 0:
                    assert(row == Common.FIRST_ROW)
                    continue
                word = self.__process_row(row)
                words.append(word)
        lesson = Lesson(self.lesson_number, False, words)
        return lesson

    def __process_row(self, row):
        hanzi, pinyin, definition1, word_type1, definition2, word_type2, _, _ = row

        word_meanings = [WordMeaning(word_type1, definition1)]
        if len(definition2) > 0:
            word_meanings.append(WordMeaning(word_type2, definition2))

        return Word(pinyin, hanzi, definition1, word_meanings, self.lesson_number)
