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


class HSK5Common:
    INPUT_FILE = 'hsk5.csv'
    OUTPUT_PATH = '/Users/pablo/Documents/CHINO/repo/confucio/create_pdf/hsk5'
    ROWS = 5
    COLUMNS = 4
    WORDS_PER_PAGE = ROWS * COLUMNS
    FONT_FAMILY = 'serif'
    FONT_WEIGHT = 'bold'
    COL_WIDTHS = [0.26, 0.06, 0.26, 0.06, 0.26, 0.06, 0.26]
    FONT_SIZES = {1: 40, 2: 40, 3: 29, 4: 22, 4.5: 21, 5: 18}
    EMPTY_HEIGHT = .08
    HEIGHTS = {
        'empty': .08,
        'chinese': .3,
        'pinyin': .1
    }

    @classmethod
    def all_words(cls):
        path = Common.HSK5_PATH + "hsk5.csv"
        reader = Reader(path, 'hsk5')
        words = reader.generate_words()
        return words

    @classmethod
    def lesson_words(cls, lesson_number):
        words = cls.all_words()
        filtered_words = [word for word in words if word.lesson_number == lesson_number]
        return filtered_words

    @classmethod
    def split_words_in_pages(cls, words):
        pages = []
        current_page = []
        for word in words:
            current_page.append(word)
            if len(current_page) == cls.WORDS_PER_PAGE:
                pages.append(current_page)
                current_page = []
        if len(current_page) > 0:
            pages.append(current_page)
        return pages

    @classmethod
    def words_to_data(cls, words):
        difference = cls.WORDS_PER_PAGE - len(words)
        for _ in range(difference):
            dummy_word = Word.dummy_word()
            words.append(dummy_word)

        data = []
        current_row = []
        for word in words:
            current_row.append(word)
            if len(current_row) == cls.COLUMNS:
                cls.append_to_data(current_row, data)
                current_row = []
        if len(current_row) > 0:
            assert(len(current_row) == cls.COLUMNS)
            cls.append_to_data(current_row, data)
        # print(data)
        return data

    @classmethod
    def append_to_data(cls, current_row, data):
        empty_row = [None for _ in current_row]
        chinese_row = [word.chinese for word in current_row]
        pinyin_row = [word.pinyin.lower() for word in current_row]
        data.append(empty_row)
        data.append(chinese_row)
        data.append(pinyin_row)

    @classmethod
    def create_plot(cls, words, words_page, page_number, real_words_count, map_sizes, lesson_number, total_pages):
        data = HSK5Common.words_to_data(words_page)
        data = cls.add_empty_cols(data)
        print(page_number)
        print(data)

        fig, ax = plt.subplots()

        # Hide axes
        # ax.xaxis.set_visible(False)
        # ax.yaxis.set_visible(False)
        plt.axis('off')

        table = ax.table(cellText=data, loc='center', cellLoc='center', colWidths=cls.COL_WIDTHS)
        table.auto_set_font_size(False)
        # table.set_fontsize(25)
        # table.scale(1, 4)

        for key, cell in table.get_celld().items():
            HSK5Common.modify_cell(key, cell, words, real_words_count, page_number, map_sizes)

        filename = 'L' + str(lesson_number) + '-' + str(page_number)
        print(HSK5Common.OUTPUT_PATH + filename)

        page_title = "HSK 5 - " + 'L' + str(lesson_number) + ' - ' + str(page_number) + "/" + str(total_pages)
        fp = FontProperties(family=cls.FONT_FAMILY, size=12)#, weight=cls.FONT_WEIGHT)

        plt.suptitle(page_title, y=1.41,fontproperties=fp)
        plt.savefig(HSK5Common.OUTPUT_PATH + "/" + filename + '.pdf', bbox_inches='tight', edgecolor=None)
        # plt.show()


    @classmethod
    def add_empty_cols(cls, data):
        new_data = []
        for row in data:
            length = len(row)
            new_row = []
            for idx, word in enumerate(row):
                new_row.append(word)
                if idx != length - 1:  # true for the last word
                    new_row.append('')
            new_data.append(new_row)
        return new_data


    @classmethod
    def modify_cell(cls, key, cell, words, real_words_count, page_number, map_sizes):
        # print(key)
        col_offset = int(key[0] / 3) * HSK5Common.COLUMNS
        map_column = {0: 0, 2: 1, 4: 2, 6: 3}

        if key[0] == 0:
            # EMPTY
            cell.set_height(cls.HEIGHTS["empty"])
            cell.visible_edges = ''

        if key[1] in [1, 3, 5]:
            cell.visible_edges = ''

        elif key[0] % 3 == 1:
            # CHINESE
            word_page_index = col_offset + map_column[key[1]] + 1
            word_index = word_page_index + HSK5Common.WORDS_PER_PAGE * (page_number - 1) # 1, 2, ...

            is_featured = False
            word = None
            if word_index <= len(words):
                word = words[word_index - 1]
                is_featured = word.is_featured

            linewidth = 1 if is_featured else 0.6
            cell.set_linewidth(linewidth)

            facecolor = "white" # "whitesmoke"
            cell.set_facecolor(facecolor)

            cell.set_height(cls.HEIGHTS["chinese"])

            font_size = HSK5Common.chinese_font_size(word_index, map_sizes, word)
            cell.set_fontsize(font_size)

            if word_page_index > real_words_count:
                cell.visible_edges = ''

        elif key[0] % 3 == 2:
            # PINYIN
            word_page_index = col_offset + map_column[key[1]] + 1
            word_index = word_page_index + HSK5Common.WORDS_PER_PAGE * (page_number - 1)

            is_featured = False
            if word_index <= len(words):
                word = words[word_index - 1]
                is_featured = word.is_featured

            linewidth = 1 if is_featured else 0.6
            cell.set_linewidth(linewidth)

            facecolor = "gainsboro" # "whitesmoke" "lemonchiffon"
            cell.set_facecolor(facecolor)

            cell.set_height(cls.HEIGHTS["pinyin"])

            font_size = HSK5Common.pinyin_font_size(word_index, map_sizes)
            cell.set_text_props(
                fontproperties=FontProperties(weight=cls.FONT_WEIGHT, size=font_size, family=cls.FONT_FAMILY)
            )

            if word_page_index > real_words_count:
                cell.visible_edges = ''

        elif key[0] != 0 and key[0] % 3 == 0:
            # empty
            cell.set_height(cls.HEIGHTS["empty"])
            cell.visible_edges = ''

    @classmethod
    def chinese_font_size(cls, word_index, map_sizes, word):
        if word is None:
            return 0 # Dummy value

        word_length = len(word.chinese)

        word_index_sizes = map_sizes.get(word_index)
        if word_index_sizes:
            word_length = word_index_sizes.get('chinese', word_length)
        fontsize = cls.FONT_SIZES[word_length]

        return fontsize

    @classmethod
    def pinyin_font_size(cls, word_index, map_sizes):
        fontsize = 12
        word_index_sizes = map_sizes.get(word_index)
        if word_index_sizes:
            fontsize = word_index_sizes.get('pinyin', fontsize)
        return fontsize
