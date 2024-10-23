#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('.')

import unicodedata
from classes.word_meaning import WordMeaning


class Word:
    SUBSTITUE = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1,
        '\xc4': 2, 'Ē': 2, 'Ī': 2, 'Ō': 2, 'Ū': 2,
        '\x80': 3, 'È': 3, 'Ì': 3, 'Ò': 3, 'Ù': 3,
        '\xc3': 4, 'É': 4, 'Í': 4, 'Ó': 4, 'Ú': 4,
        '\xc7': 5, 'Ě': 5, 'Ǐ': 5, 'Ǒ': 5, 'Ǔ': 5
    }

    def __init__(self, pinyin, chinese, definition, word_meanings, word_number, lesson_number, is_featured):
        input_list = [pinyin, chinese, definition]
        decoded_list = [self.decode(val) for val in input_list]
        self.pinyin, self.chinese, self.definition = input_list
        self.pinyin_d, self.chinese_d, self.definition_d = decoded_list
        self.pinyin_l, self.chinese_l, self.definition_l = [len(val) for val in decoded_list]
        self.word_meanings = word_meanings
        self.number = word_number
        self.lesson_number = lesson_number
        self.is_featured = is_featured

    def keys(self):
        return [word_meaning.word_type.key for word_meaning in self.word_meanings]

    @classmethod
    def dummy_word(cls):
        return Word('', '', '', '', '', '', '')

    @classmethod
    def decode(cls, word):
        return word  # .decode("utf-8")

    @classmethod
    def min_lenght(cls, word, min_len=0):
        return word if min_len == 0 else word + " "*(min_len - len(word))

    def str_all(self, min_len=[0, 0]):
        if self.word_types is None:
            # TODO: remove
            pinyin = self.min_lenght(self.pinyin_d, min_len[0])
            chinese = self.min_lenght(self.chinese_d, min_len[1])
            space_before = " "*(min_len[1] - len(self.chinese_d))
            space_after = " "*len(self.chinese_d)
            string = '%s %s %s"%s"%s' % (pinyin, chinese, space_before, self.definition_d, space_after)
            return string
        else:
            # TODO
            return ""

    def str_pinyin(self):
        return self.pinyin_d

    def str_chinese(self):
        return self.chinese_d + " "*len(self.chinese_d)

    def str_definition(self):
        return self.definition_d

    @classmethod
    def sorted(cls, word_list):
        return sorted(word_list, cmp=Word.compare)

    @classmethod
    def begin_with(cls, word_list, character):
        array = []
        for word in word_list:
            first_character = cls.strip_accents(word.pinyin)[0]
            if first_character == character:
                array.append(word)
        return array

    # @staticmethod
    # def sort_lambda(text):
    #     # for key, value in Word.SUBSTITUE.iteritems():
    #     #     text = text.replace(key, value)
    #     return Word.strip_accents(text)  # + 'Z'

    @staticmethod
    def compare(word1, word2):

        text1, text2 = word1.pinyin, word2.pinyin
        text1_plain, text2_plain = Word.strip_accents(text1), Word.strip_accents(text2)

        if text1_plain < text2_plain:
            # print text1 + " < " + text2
            return -1
        else:
            # print text2 + " < " + text1
            return 1

        #
        # longest_length = min(len(text1_plain), len(text2_plain))
        # longest_length_2 = min(len(text1_plain), len(text2_plain))
        # print
        # print(text1_plain + " " + word1.word_meanings[0].word_meaning_str)
        # print(text2_plain + " " + word2.word_meanings[0].word_meaning_str)
        #
        # print(len(text1))
        # print(len(text2))
        # print(len(text1_plain))
        # print(len(text2_plain))
        #
        # print(text1[0])
        # print(text1[1])
        # print(ord(text1[2]))
        # print(text1[3])
        # exit(1)
        #
        # for x in range(longest_length):
        #     char1, char2 = text1[x], text2[x]
        #     char1_plain, char2_plain = text1_plain[x], text2_plain[x]
        #
        #     print(x)
        #     if char1 != char1_plain:
        #         print('1 => ' + char1 + " " + char1_plain)
        #         Word.SUBSTITUE[char1]
        #     if char2 != char2_plain:
        #         print('2 => ' + char2 + " " + char2_plain)
        #         Word.SUBSTITUE[char2]
        #
        # # return 1
        #
        # for x in range(longest_length):
        #     char1, char2 = text1[x], text2[x]
        #     char1_plain, char2_plain = text1_plain[x], text2_plain[x]
        #
        #     print(x)
        #     print('1 => ' + char1 + " " + char1_plain)
        #     print('2 => ' + char2 + " " + char2_plain)
        #
        #     if char1 == char2:
        #         print('char1 == char2')
        #         continue
        #
        #     # char1 != char2
        #     if char1_plain != char2_plain:
        #         print('char1_plain != char2_plain')
        #         return ord(char1_plain) - ord(char2_plain)
        #
        #     # char1_plain == char2_plain
        #     print('char1_plain == char2_plain')
        #     Word.SUBSTITUE[char1]
        #     Word.SUBSTITUE[char2]
        #     return Word.SUBSTITUE[char1] - Word.SUBSTITUE[char2]

    #
    # SOURCE: https://stackoverflow.com/a/31607735/4547232
    #
    @staticmethod
    def strip_accents(text):
        """
        Strip accents from input String.

        :param text: The input string.
        :type text: String.

        :returns: The processed String.
        :rtype: String.
        """
        try:
            text = unicode(text, 'utf-8')
        except (TypeError, NameError):  # unicode is a default on python 3
            pass
        text = unicodedata.normalize('NFD', text)
        text = text.encode('ascii', 'ignore')
        text = text.decode("utf-8")
        return str(text)
