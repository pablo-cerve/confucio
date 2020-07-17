import sys
sys.path.append('.')

import csv
from csv_utils.common import Common


class Writer:
    @staticmethod
    def write_lessons(path, lessons):
        word_arrays = []
        for lesson in lessons:
            word_arrays.append(lesson.words)
        Writer.write_words(path, word_arrays)

    @staticmethod
    def write_lesson(lesson):
        lesson_path = Common.lesson_path(lesson)
        lesson_words = lesson.words
        Writer.write_words(lesson_path, [lesson_words])

    @staticmethod
    def write_words(path, word_arrays):
        with open(path, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(Common.FIRST_ROW)
            for word_array in word_arrays:
                count = 1
                for word in word_array:
                    row = Writer.__word_row(word) + [count]
                    writer.writerow(row)
                    count += 1

    @staticmethod
    def __word_row(word):
        definition1, word_type1, definition2, word_type2 = Writer.__word_attributes(word)
        row = [word.chinese, word.pinyin, definition1, word_type1, definition2, word_type2, word.lesson_id]
        return row

    @staticmethod
    def __word_attributes(word):
        definition1, word_type1 = Writer.__definition_and_word_type(word.word_meanings[0])
        if len(word.word_meanings) == 1:
            return definition1, word_type1, None, None

        definition2, word_type2 = Writer.__definition_and_word_type(word.word_meanings[1])
        return definition1, word_type1, definition2, word_type2

    @staticmethod
    def __definition_and_word_type(word_meaning):
        word_type = word_meaning.word_type.key
        definition = word_meaning.word_meaning_str
        return definition, word_type
