import sys
sys.path.append('.')

import numpy as np
import matplotlib
matplotlib.rcParams['font.family'] = ['Heiti TC']

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from csv_utils.common import Common
from csv_utils.reader import Reader
from classes.word import Word
from create_pdf.hsk5_common import HSK5Common


class CreatePDFHSK5Lesson:
    MAP_SIZES = {
        1: {
            15: {'chinese': 4, 'pinyin': 10},
            18: {'chinese': 3},
            24: {'chinese': 4, 'pinyin': 11},
            38: {'chinese': 4, 'pinyin': 9}
        },
        2: {
            2:  {'chinese': 3},
            16: {'chinese': 3}
        },
        3: {
            24: {'chinese': 3},
            43: {'chinese': 4},
            44: {'chinese': 3}
        },
        4: {}
    }

    def __init__(self, lesson_number):
        map_sizes = self.MAP_SIZES[lesson_number]
        words = HSK5Common.lesson_words(lesson_number)
        word_pages = HSK5Common.split_words_in_pages(words, HSK5Common.WORDS_PER_PAGE)
        filename_common = '/L' + str(lesson_number) + '-'

        for idx, words_page in enumerate(word_pages):
            real_words_count = len(words_page)
            data = HSK5Common.words_to_data(words_page)
            page_number = idx + 1
            filename = filename_common + str(page_number) + '.pdf'
            HSK5Common.create_plot(data, page_number, real_words_count, filename, map_sizes)


CreatePDFHSK5Lesson(1)
CreatePDFHSK5Lesson(2)
CreatePDFHSK5Lesson(3)
CreatePDFHSK5Lesson(4)
