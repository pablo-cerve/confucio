import sys
sys.path.append('.')

import math
import os
import unidecode
from file_utils.text_utils.text_file_reader import TextFileReader
from file_utils.csv_utils.csv_reader import CSVReader


class HSKCheck:
    CHINO_PATH = "/Users/pablocerve/Documents/CHINO"
    MY_FILE_PATH = CHINO_PATH + "/repo/confucio/lessons/hsk3"
    MY_FILE_FILENAME = "hsk3.csv"

    OFFICIAL_PATH = CHINO_PATH + "/HSK3/palabras/official_list"
    IMAGES_PATH = CHINO_PATH + "/HSK3/palabras/oficiales"

    @classmethod
    def compare_with_official(cls):
        official_words = cls.get_official_words("HSK3.txt")
        assert(len(official_words) == 600)

        my_words = cls.get_my_words(0)
        assert(len(my_words) == 600)

        assert(official_words == my_words)
        print("compare_with_official - SUCCESS!")

        # official_not_my = list(set(official_words) - set(my_words))
        # official_not_my_length = len(official_not_my)
        # print("official_not_my - " + str(official_not_my_length))
        # assert(official_not_my_length == 0)
        # cls.print_array(official_not_my)
        #
        # print
        #
        # my_not_official = list(set(my_words) - set(official_words))
        # my_not_official_length = len(my_not_official)
        # print("my_not_official - " + str(my_not_official_length))
        # assert(my_not_official_length == 0)
        # cls.print_array(my_not_official)

        # prev = 1
        # for idx, word in enumerate(official_words):
        #     my_word = my_words[idx]
        #     if my_word != word:
        #         if idx != prev + 1:
        #             print(idx, word, my_word)
        #         prev = idx

    @classmethod
    def compare_with_images(cls):
        my_pinyin = cls.get_my_words(1)
        assert(len(my_pinyin) == 600)
        my_pinyin = [unidecode.unidecode(word) for word in my_pinyin]

        words = cls.get_images()
        assert(len(words) == 600)
        words = [word.upper() for word in words]
        words = [unidecode.unidecode(word) for word in words]

        assert(my_pinyin == words)
        print("compare_with_images - SUCCESS!")

        # for idx, word in enumerate(words):
        #     pinyin = my_pinyin[idx]
        #     word_upper = word.upper()
        #     pinyin_un = unidecode.unidecode(pinyin)
        #     word_un = unidecode.unidecode(word_upper)
        #     if pinyin_un != word_un:
        #         print(idx + 1, pinyin_un, word_un)
        #         assert(pinyin_un == word_un)

    ######################################################################

    @classmethod
    def print_array(cls, array):
        for word in array:
            print(word)

    @classmethod
    def get_official_words(cls, filename):
        file = TextFileReader(cls.OFFICIAL_PATH, filename)
        array = []
        while file.continue_reading:
            word = file.read_line().strip()
            array.append(word)
        return array

    @classmethod
    def get_my_words(cls, column_number):
        lines = CSVReader(cls.MY_FILE_PATH, cls.MY_FILE_FILENAME).lines
        array = []
        lines.pop(0)
        for line in lines:
            word = line[column_number].strip()
            array.append(word)
        return array

    @classmethod
    def get_images(cls):
        words = []
        for folder_name in sorted(os.listdir(cls.IMAGES_PATH)):
            if ".DS_Store" in folder_name:
                continue
            # print(folder_name)
            for image_name in sorted(os.listdir(cls.IMAGES_PATH + "/" + folder_name)):
                if ".DS" in image_name:
                    continue
                word_start = image_name.find("-") + 1
                word_end = image_name.find("_")
                word = image_name[word_start:word_end]
                # print(word)
                words.append(word)
        return words
