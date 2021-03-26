import sys
sys.path.append('.')

import math
import os
from file_utils.text_utils.text_file_reader import TextFileReader
from file_utils.csv_utils.csv_reader import CSVReader


class HSKCheck:
    MY_FILE_PATH = "/Users/pablocerve/Documents/CHINO/repo/confucio/lessons/hsk3"
    MY_FILE_FILENAME = "hsk3.csv"

    OFFICIAL_PATH = "/Users/pablocerve/Documents/CHINO/HSK3/official_list"
    IMAGES_PATH = "/Users/pablocerve/Documents/CHINO/HSK3/palabras"

    @classmethod
    def compare_with_official(cls):
        official_words = cls.get_official_words("HSK3.txt")
        assert(len(official_words) == 600)

        my_words = cls.get_my_words(0)
        # assert(len(my_words) == 600)

        official_not_my = list(set(official_words) - set(my_words))
        official_not_my_length = len(official_not_my)
        print("official_not_my - " + str(official_not_my_length))
        assert(official_not_my_length == 0)
        cls.print_array(official_not_my)

        print

        my_not_official = list(set(my_words) - set(official_words))
        print("my_not_official - " + str(len(my_not_official)))
        cls.print_array(my_not_official)

    @classmethod
    def compare_with_images(cls):
        my_pinyin = cls.get_my_words(1)
        print(len(my_pinyin))

        words = cls.get_images()
        print(len(words))

        print(words)
        for idx, word in enumerate(words):
            pinyin = my_pinyin[idx]
            print(idx, pinyin, word.upper())

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
                print(word)
                words.append(word)
        return words


HSKCheck.compare_with_official()
HSKCheck.compare_with_images()
