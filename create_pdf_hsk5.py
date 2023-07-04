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
# from reportlab.platypus import SimpleDocTemplate, TableStyle, Table, Image as ImageDoc, PageBreak, Spacer, Paragraph
# from reportlab.lib.units import cm, inch


class CreatePDFHSK5:
    INPUT_PATH = '/Users/pablocerve/Documents/CHINO/repo/confucio/lessons/hsk5'
    INPUT_FILE = 'hsk5.csv'
    OUTPUT_PATH = '/Users/pablocerve/Documents/CHINO/HSK5/palabras'
    ROWS = 5
    COLUMNS = 4
    WORDS_PER_PAGE = ROWS * COLUMNS

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
    def __init__(self):
        # self.doc = self.create_doc()
        pass

    def run(self, lesson_number):
        self.lesson_number = lesson_number
        self.map_sizes = self.MAP_SIZES[lesson_number]
        words = self.lesson_words()
        word_pages = self.split_words_in_pages(words, self.WORDS_PER_PAGE)

        for idx, words_page in enumerate(word_pages):
            real_words_count = len(words_page)
            data = self.words_to_data(words_page)
            self.create_plot(data, idx + 1, real_words_count)

    @classmethod
    def split_words_in_pages(cls, words, page_length):
        pages = []
        current_page = []
        for word in words:
            current_page.append(word)
            if len(current_page) == page_length:
                pages.append(current_page)
                current_page = []
        if len(current_page) > 0:
            pages.append(current_page)
        return pages

    def lesson_words(self):
        path = Common.HSK5_PATH + "hsk5.csv"
        reader = Reader(path, 'hsk5')
        words = reader.generate_words()
        filtered_words = [word for word in words if word.lesson_number == self.lesson_number]
        return filtered_words

    @classmethod
    def words_to_data(cls, words):
        difference = cls.WORDS_PER_PAGE - len(words)
        for _ in range(difference):
            dummy_word = Word('', '', '', '', '', '', '')
            words.append(dummy_word)

        data = []
        current_row = []
        for word in words:
            current_row.append(word)
            if len(current_row) == cls.COLUMNS:
                cls.append_to_data(current_row, data)
                current_row = []
        if len(current_row) > 0:
            cls.append_to_data(current_row, data)
        print(data)
        return data

    @classmethod
    def append_to_data(cls, current_row, data):
        empty_row = [None for _ in current_row]
        chinese_row = [word.chinese for word in current_row]
        pinyin_row = [word.pinyin.lower() for word in current_row]
        data.append(empty_row)
        data.append(chinese_row)
        data.append(pinyin_row)

    def create_plot(self, data, page_number, real_words_count):
        fig, ax = plt.subplots()

        # Hide axes
        # ax.xaxis.set_visible(False)
        # ax.yaxis.set_visible(False)
        plt.axis('off')

        new_data = []
        for row in data:
            length = len(row)
            new_row = []
            for idx, word in enumerate(row):
                new_row.append(word)
                if idx != length - 1:  # true for the last word
                    new_row.append('')
            new_data.append(new_row)

        colWidths = [0.26, 0.06, 0.26, 0.06, 0.26, 0.06, 0.26]
        table = ax.table(cellText=new_data, loc='center', cellLoc='center', colWidths=colWidths)
        table.auto_set_font_size(False)
        # table.set_fontsize(25)
        # table.scale(1, 4)

        for key, cell in table.get_celld().items():
            self.improve_cell(key, cell, real_words_count, page_number)

        filename = '/L' + str(self.lesson_number) + '-' + str(page_number) + '.pdf'
        plt.savefig(self.OUTPUT_PATH + filename, bbox_inches='tight', edgecolor=None)
        # plt.show()

    def improve_cell(self, key, cell, real_words_count, page_number):
        # print(key)
        col_offset = int(key[0] / 3) * self.COLUMNS
        map_column = {0: 0, 2: 1, 4: 2, 6: 3}

        if key[0] == 0:
            # EMPTY
            cell.set_height(.08)
            cell.visible_edges = ''

        if key[1] in [1, 3, 5]:
            cell.visible_edges = ''
        elif key[0] % 3 == 1:
            # CHINESE
            word_page_index = col_offset + map_column[key[1]] + 1
            word_index = word_page_index + self.WORDS_PER_PAGE * (page_number - 1)

            cell.set_height(.3)
            cell.set_fontsize(self.chinese_font_size(word_index))

            if word_page_index > real_words_count:
                cell.visible_edges = ''

        elif key[0] % 3 == 2:
            # PINYIN
            word_page_index = col_offset + map_column[key[1]] + 1
            word_index = word_page_index + self.WORDS_PER_PAGE * (page_number - 1)

            cell.set_height(.1)
            cell.set_facecolor("lemonchiffon")  # cell.set_facecolor("#ffffce")
            cell.set_text_props(
                fontproperties=FontProperties(weight='bold', size=self.pinyin_font_size(word_index), family='serif')
            )

            if word_page_index > real_words_count:
                cell.visible_edges = ''

        elif key[0] != 0 and key[0] % 3 == 0:
            # empty
            cell.set_height(.08)
            cell.visible_edges = ''

    def chinese_font_size(self, word_index):
        fontsize = 40
        word_index_sizes = self.map_sizes.get(word_index)
        if word_index_sizes:
            number_of_letters = word_index_sizes.get('chinese', 2)
            fontsize = {2: 40, 3: 29, 4: 22}[number_of_letters]
        return fontsize

    def pinyin_font_size(self, word_index):
        fontsize = 12
        word_index_sizes = self.map_sizes.get(word_index)
        if word_index_sizes:
            fontsize = word_index_sizes.get('pinyin', fontsize)
        return fontsize

CreatePDFHSK5().run(1)
CreatePDFHSK5().run(2)
CreatePDFHSK5().run(3)
CreatePDFHSK5().run(4)