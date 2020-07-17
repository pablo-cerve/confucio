import string
from classes.lesson import Lesson
from classes.word import Word
from classes.book import Book


class SortAlpha:
    def __init__(self, book_number):
        self.current_letter = None
        self.current_words = []
        self.word_list = []
        for lesson_num in Book.book_lesson_numbers(book_number):
            lesson = Lesson(lesson_num)
            self.word_list += lesson.words

    def run(self):
        characters = list(string.ascii_uppercase)
        print(characters)

        for character in characters:
        # for character in ['B']:
            character_words = Word.begin_with(self.word_list, character)
            total_words = len(character_words)
            if total_words == 0:
                continue
            self.print_character(character, total_words)

            word_list = Word.sorted(character_words)
            for word in word_list:
                self.print_word(word)

    @staticmethod
    def print_character(character, total_words):
        symbols_line = "=" * 33
        symbols = "=" * 15
        print symbols_line
        print symbols + " " + character + " " + symbols + " count: " + str(total_words)
        print symbols_line

    @staticmethod
    def print_word(word):
        word_chars = 12
        word_length = len(Word.strip_accents(word.pinyin))
        word_str = word.pinyin + " " * (word_chars - word_length)

        word_type_chars = 10
        word_type = word.word_meanings[0].word_type.book_type
        word_type_str = word_type + " " * (word_type_chars - len(word_type))

        space_str = (" " if len(str(word.lesson_number)) == 1 else "")
        lesson_str = space_str + str(word.lesson_number)

        print word_str + " " + word_type_str + " " + lesson_str

SortAlpha(1).run()
# SortAlpha(2).run()
