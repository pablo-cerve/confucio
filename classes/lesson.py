#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import shuffle
from lessons.book import Book
from word import Word


class Lesson:
    def __init__(self, lesson_id, extra=False, words=None):
        self.extra = extra
        self.lesson_id = lesson_id
        self.book_number = Lesson.book_number(lesson_id)
        self.words = words if words is not None else self.__read_words(lesson_id, extra)
        self.max_lenghts = [max([word.pinyin_l for word in self.words]), max([word.chinese_l for word in self.words])]

    @staticmethod
    def book_number(lesson_id):
        return 1 if lesson_id < 15 else 2

    @staticmethod
    def __read_words(lesson_id, extra):
        words = []
        for word_s in Book.get_lesson(lesson_id - 1, extra):
            # TODO: fix
            if len(word_s) == 3:
                if isinstance(word_s[2], list):
                    pinyin, chinese, word_types = word_s
                    word = Word(pinyin, chinese, "", word_types)
                else:
                    pinyin, chinese, definition = word_s
                    word_types = None
                    word = Word(pinyin, chinese, definition, word_types)
            else:
                pinyin, chinese, definition, word_types = word_s
                word = Word(pinyin, chinese, definition, word_types)

            word.set_lesson_id(lesson_id)
            words.append(word)
        return words

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
        lesson_str = str(self.lesson_id)
        if self.extra:
            lesson_str += " [extra]"
        print "LECCIÓN %s %s %s" % (lesson_str, extra_str, random_str)

    def _print_aux(self, title, rand, method_str):
        self._print_lesson_id(title, rand)
        words_list = self.words if not rand else self._shuffled_words()
        for idx, word in enumerate(words_list):
            func = getattr(word, method_str)
            if method_str == "str_definition":
                if word.word_meanings is None:
                    # TODO: remove
                    print self.index_str(idx, word.str_definition())
                else:
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
