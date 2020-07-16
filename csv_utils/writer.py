import sys
sys.path.append('.')

import csv

from csv_utils.common import Common


class Writer:
    def __init__(self, book_number, lesson_number, lesson):
        self.book_number = book_number
        self.lesson_number = lesson_number
        self.lesson = lesson
        self.path = Common.lesson_path(book_number, lesson_number) + ("_extra" if self.lesson.extra else "") + ".csv"

    def save_csv(self):
        with open(self.path, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(Common.FIRST_ROW)

            for word in self.lesson.words:
                definition1, word_type1, definition2, word_type2 = self.__word_attributes(word)
                writer.writerow([word.chinese, word.pinyin, definition1, word_type1, definition2, word_type2])

    def __word_attributes(self, word):
        definition1, word_type1 = self.__definition_and_word_type(word.word_meanings[0])
        if len(word.word_meanings) == 1:
            return definition1, word_type1, None, None

        definition2, word_type2 = self.__definition_and_word_type(word.word_meanings[1])
        return definition1, word_type1, definition2, word_type2

    def __definition_and_word_type(self, word_meaning):
        word_type = word_meaning.word_type.key
        definition = word_meaning.word_meaning_str
        return definition, word_type
