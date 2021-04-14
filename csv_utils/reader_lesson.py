import sys
sys.path.append('.')

import csv

from classes.word import Word
from classes.word_meaning import WordMeaning
from csv_utils.common import Common
from csv_utils.reader import Reader


class ReaderLesson:
    def __init__(self, book_number, lesson_number, lesson_extra=False):
        self.book_number = book_number
        path = Common.book_lesson_path(book_number, lesson_number, lesson_extra)
        self.reader = Reader(path, lesson_number)
        print(path)

    def generate_words(self):
        return self.reader.generate_words()
