#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('.')

from random import shuffle
from classes.book import Book
from classes.word import Word
from csv_utils.reader_lesson import ReaderLesson
from classes.printer import Printer


class Lesson:
    def __init__(self, lesson_number, extra=False):
        self.extra = extra
        self.lesson_number = lesson_number
        self.book_number = Book.book_number(lesson_number)
        self.words = ReaderLesson(self.book_number, lesson_number, extra).generate_words()

    def get_words(self, word_keys=None):
        return Printer.get_words(self.words, word_keys)

    def print_all(self, rand=False):
        self._print_lesson_number("completa", rand)
        Printer.print_all(words, rand)

    def print_pinyin(self, rand=False):
        self._print_lesson_number("completa", rand)
        Printer.print_pinyin(self.words, rand)

    def print_chinese(self, rand=False):
        self._print_lesson_number("completa", rand)
        Printer.print_chinese(self.words, rand)

    def print_definition(self, rand=False):
        self._print_lesson_number("completa", rand)
        Printer.print_definition(self.words, rand)

    def _print_lesson_number(self, extra_str, rand):
        extra_str = "- " + extra_str
        random_str = "- RANDOM!!" if rand else ""
        lesson_str = str(self.lesson_number)
        if self.extra:
            lesson_str += " [extra]"
        print("LECCIÓN %s %s %s" % (lesson_str, extra_str, random_str))
