#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('.')

from random import shuffle
from classes.book import Book
from classes.word import Word
from classes.word_type import WordType
from csv_utils.reader_lesson import ReaderLesson


class Printer:
    def __init__(self, lesson_number, extra=False):
        self.extra = extra
        self.lesson_number = lesson_number
        self.book_number = Book.book_number(lesson_number)
        self.words = ReaderLesson(self.book_number, lesson_number, extra).generate_words()
        self.max_lenghts = [max([word.pinyin_l for word in self.words]), max([word.chinese_l for word in self.words])]

    @classmethod
    def get_words(cls, words_input, word_keys=None):
        if word_keys is None:
            return self.words

        words = []
        set_word_keys = set(word_keys)
        for word in words_input:
            if set(word.keys()) & set_word_keys:
                words.append(word)
        return words

    @classmethod
    def print_all(cls, words, rand=False):
        print
        max_lenghts = [max([word.pinyin_l for word in words]), max([word.chinese_l for word in words])]
        words_list = words if not rand else self._shuffled_words()
        for idx, word in enumerate(words_list):
            print(cls.index_str(idx, word.str_all(max_lenghts)))
        print

    @classmethod
    def print_pinyin(cls, words, rand=False):
        cls._print_aux(words, rand, "str_pinyin")

    @classmethod
    def print_chinese(cls, words, rand=False):
        cls._print_aux(words, rand, "str_chinese")

    @classmethod
    def print_definition(cls, words, rand=False):
        cls._print_aux(words, rand, "str_definition")

    @classmethod
    def print_definition_hsk4(cls, words, rand=False):
        cls._print_aux(words, rand, "str_definition", True)

    @classmethod
    def index_str(cls, index, string):
        if isinstance(index, str):
            # python3 lessons/run_hsk4.py
            space = " " if len(index) == 1 else ""
        else:
            # python3 lessons/run_hsk3.py
            index += 1
            space = " " if index < 10 else ""
        return "%s(%s) %s" % (space, str(index), string)


    @classmethod
    def _print_aux(cls, words, rand, method_str, lesson_num=False):
        words_list = words if not rand else cls._shuffled_words(words)
        for idx, word in enumerate(words_list):
            func = getattr(word, method_str)
            if method_str == "str_definition":
                estring = cls._append_meaning(word)
                idx = word.number if lesson_num else idx
                if lesson_num and idx == '1':
                    cls.print_lesson_number(word.lesson_number)
                if cls._must_print(word):
                    print(cls.index_str(idx, estring))
            else:
                print(cls.index_str(idx, func()))
        print

    @classmethod
    def _must_print(cls, word):
        return True
        # word_types = [x.word_type.key for x in word.word_meanings]
        # print(word_types)

        # word_type_keys = set(WordType.TYPES_HASH.keys() - ["ADV", "CLA", "PRO", "NOM", "VER", "ADJ"])
        # return not word.is_featured and word_type_keys & set(word_types)

        # return not word.is_featured and 'PRO' in word_types
        # return word.is_featured

    @classmethod
    def _append_meaning(cls, word):
        estring = ""
        for wm_idx, word_meaning in enumerate(word.word_meanings):
            word_types_str = ""
            if word.is_featured:
                word_types_str += "[*****]"
            word_types_str += "[" + word_meaning.word_type.type + "] " + word_meaning.word_meaning_str
            estring += word_types_str  # str(word_types_str, 'utf-8')
            if wm_idx + 1 != len(word.word_meanings):
                estring += " --- "
        return estring


    @classmethod
    def _shuffled_words(cls, words_input):
        # copy the list so the order of self.words is not altered
        words = []
        [words.append(word) for word in words_input]
        shuffle(words)
        return words

    @classmethod
    def print_lesson_number(cls, lesson_number):
        # print("###################################################################")
        print("############################ LESSON %s ############################" % str(lesson_number))
        # print("###################################################################")
