#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import shuffle
from lessons.auxi import get_lesson
from word import Word


class Lesson:
    def __init__(self, lesson_id):
        self.lesson_id = lesson_id
        self.words = []
        for word_s in get_lesson(lesson_id - 1):
            pinyin, chinese, definition = word_s
            word = Word(pinyin, chinese, definition)
            self.words.append(word)
        self.max_lenghts = [max([word.pinyin_l for word in self.words]), max([word.chinese_l for word in self.words])]

    def print_all(self, rand=False):
        print
        self._print_lesson_id("completa", rand)
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

    def _print_lesson_id(self, extra_str, rand):
        extra_str = "- " + extra_str
        random_str = "- RANDOM!!" if rand else ""
        print "LECCIÓN %s %s %s" % (self.lesson_id, extra_str, random_str)

    def _print_aux(self, title, rand, method_str):
        print
        self._print_lesson_id(title, rand)
        words_list = self.words if not rand else self._shuffled_words()
        for idx, word in enumerate(words_list):
            func = getattr(word, method_str)
            print self.index_str(idx, func())
        print

    def _shuffled_words(self):
        # copy the list so the order of self.words is not altered
        words = []
        [words.append(word) for word in self.words]
        shuffle(words)
        return words
