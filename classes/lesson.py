#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('.')

from random import shuffle
from classes.book import Book
from word import Word
from csv_utils.reader import Reader


class Lesson:
    def __init__(self, lesson_number, extra=False):
        self.extra = extra
        self.lesson_number = lesson_number
        self.book_number = Book.book_number(lesson_number)
        self.words = Reader(self.book_number, lesson_number, extra).generate_words()
        self.max_lenghts = [max([word.pinyin_l for word in self.words]), max([word.chinese_l for word in self.words])]

    def get_words(self, word_keys=None):
        if word_keys is None:
            return self.words

        words = []
        set_word_keys = set(word_keys)
        for word in self.words:
            if set(word.keys()) & set_word_keys:
                words.append(word)
        return words

    def print_all(self, rand=False):
        print
        self._print_lesson_number("completa", rand)
        words_list = self.words if not rand else self._shuffled_words()
        for idx, word in enumerate(words_list):
            print self.index_str(idx, word.str_all(self.max_lenghts))
        print

    def print_pinyin(self, rand=False):
        self._print_aux("pinyin", rand, "str_pinyin")

    def print_chinese(self, rand=False):
        self._print_aux("chino", rand, "str_chinese")

    def print_definition(self, rand=False):
        self._print_aux("definiciones", rand, "str_definition")

    @classmethod
    def index_str(cls, index, string):
        space = " " if index < 9 else ""
        return "%s(%s) %s" % (space, index + 1, string)

    def _print_lesson_number(self, extra_str, rand):
        extra_str = "- " + extra_str
        random_str = "- RANDOM!!" if rand else ""
        lesson_str = str(self.lesson_number)
        if self.extra:
            lesson_str += " [extra]"
        print "LECCIÓN %s %s %s" % (lesson_str, extra_str, random_str)

    def _print_aux(self, title, rand, method_str):
        self._print_lesson_number(title, rand)
        words_list = self.words if not rand else self._shuffled_words()
        for idx, word in enumerate(words_list):
            func = getattr(word, method_str)
            if method_str == "str_definition":
                estring = ""
                for wm_idx, word_meaning in enumerate(word.word_meanings):
                    word_types_str = "[" + word_meaning.word_type.type + "] " + word_meaning.word_meaning_str
                    estring += unicode(word_types_str, 'utf-8')
                    if wm_idx + 1 != len(word.word_meanings):
                        estring += " --- "
                print self.index_str(idx, estring)
            else:
                print self.index_str(idx, func())
        print

    def _shuffled_words(self):
        # copy the list so the order of self.words is not altered
        words = []
        [words.append(word) for word in self.words]
        shuffle(words)
        return words
