import sys
sys.path.append('.')

import csv

from classes.lesson import Lesson
from classes.word import Word
from classes.word_meaning import WordMeaning


class Reader:
    LESSONS_PATH = "/Users/pablocerve/Documents/CHINO/repo/confucio/lessons"
    FIRST_ROW = ['HANZI', 'PINYIN', 'DEF1', 'TIPO1', 'DEF2', 'TIPO2']

    def __init__(self, book_number, lesson_number):
        self.book_number = book_number
        self.lesson_number = lesson_number
        self.path = self.LESSONS_PATH + "/book" + str(book_number) + "/lesson" + str(lesson_number) + ".csv"
        print(self.path)

    def generate_lesson(self):
        words = []
        with open(self.path) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for index, row in enumerate(reader):
                if index == 0:
                    assert(row == self.FIRST_ROW)
                    continue
                word = self.__process_row(row)
                words.append(word)
        lesson = Lesson(self.lesson_number, False, words)
        return lesson

    def __process_row(self, row):
        hanzi, pinyin, definition1, word_type1, definition2, word_type2 = row

        word_meanings = [WordMeaning(word_type1, definition1, self.book_number)]
        if len(definition2) > 0:
            word_meanings.append(WordMeaning(word_type2, definition2, self.book_number))

        return Word(pinyin, hanzi, definition1, word_meanings, self.lesson_number)
