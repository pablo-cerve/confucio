import sys
sys.path.append('.')

import numpy as np
import matplotlib

print(matplotlib.rcParams)

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from csv_utils.common import Common
from csv_utils.reader import Reader
from classes.word import Word
# from reportlab.platypus import SimpleDocTemplate, TableStyle, Table, Image as ImageDoc, PageBreak, Spacer, Paragraph
# from reportlab.lib.units import cm, inch


class CreatePDF:
    ROWS = 5
    COLUMNS = 4
    WORDS_PER_PAGE = ROWS * COLUMNS

    TITLE_FONT_FAMILY = 'serif'
    FONT_SIZES = {1: 40, 2: 40, 3: 29, 4: 22, 4.5: 21, 5: 18, 6: 15}

    COL_WIDTHS = [0.26, 0.06, 0.26, 0.06, 0.26, 0.06, 0.26]
    EMPTY_HEIGHT = .08
    # HEIGHTS = {
    #     'empty': .08,
    #     'chinese': .3,
    #     'pinyin': .1
    # }
    HEIGHTS = {
        'empty': .08,
        'definitions': .14,
        'chinese': .18,
        'pinyin': .08
    }

    @classmethod
    def words(cls, key):
        path = Common.hsk_csv_path(key)
        reader = Reader(path, key)
        words = reader.generate_words()
        return words

    @classmethod
    def lesson_words(cls, key, lesson_number):
        words = cls.words(key)
        lesson_words = [word for word in words if word.lesson_number == lesson_number]
        return lesson_words

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
        definition_row, chinese_row, pinyin_row = [], [], []
        for word in current_row:
            definition = cls._definition(word)
            definition_row.append(definition)
            chinese_row.append(word.chinese)
            pinyin_row.append(word.pinyin.lower())

        data.append(empty_row)
        data.append(pinyin_row)
        data.append(chinese_row)
        data.append(definition_row)

    @classmethod
    def _definition(cls, word):
        definition = ""
        for word_meaning in word.word_meanings:
            if len(definition) > 0:
                definition += "\n"
            definition += "[" + word_meaning.word_type.short_word_type() + "] " + word_meaning.word_meaning_str
        return definition

    @classmethod
    def create_plot(cls, pdf_filename, words, words_page, page_number, real_words_count, map_sizes, lesson_number, total_pages, titles_dict):
        data = CreatePDF.words_to_data(words_page)
        data = cls.add_empty_cols(data)
        # print(page_number)
        # print(data)

        fig, ax = plt.subplots()

        # Hide axes
        # ax.xaxis.set_visible(False)
        # ax.yaxis.set_visible(False)
        plt.axis('off')

        table = ax.table(cellText=data, loc='center', cellLoc='center', colWidths=cls.COL_WIDTHS)
        table.auto_set_font_size(False)

        for key, cell in table.get_celld().items():
            CreatePDF.modify_cell(ax, key, cell, words, real_words_count, page_number, map_sizes)

        cls._page_title(plt, lesson_number, page_number, total_pages, titles_dict)
        plt.savefig(pdf_filename, bbox_inches='tight', edgecolor=None)


    @classmethod
    def create_plot2(cls, pdf_filename, words, words_page, page_number, real_words_count, map_sizes, lesson_number, total_pages, titles_dict):
        data = CreatePDF.words_to_data(words_page)
        # data = cls.add_empty_cols(data)
        # print(page_number)
        # print(data)

        nrows, ncols = 5, 4
        figsize = (11.69, 8.27)
        fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)

        row_i, col_i = 0, 0
        for word_page_index, word in enumerate(words_page):
            ax_i = ax[row_i][col_i]
            pinyin = word.pinyin.lower()
            chinese = word.chinese
            definition = cls._definition(word)

            table = ax_i.table(
                cellText=[[chinese], [definition]],
                colLabels=[pinyin],
                colWidths=[0.26],
                loc='center'
            )
            ax_i.axis("off")

            for key, cell in table.get_celld().items():
                cls.modify_cell2(key, cell, word, word_page_index, page_number, map_sizes)

            col_i += 1
            if col_i == 4:
                row_i += 1
                col_i = 0

        pdf_filename += "a.pdf"
        plt.savefig(pdf_filename, bbox_inches='tight', edgecolor=None)
        sss

        # print(len(ax))
        # print(len(ax[0]))
        # print(len(data))


    @classmethod
    def modify_cell2(cls, key, cell, word, word_page_index, page_number, map_sizes):
        row_index = key[0]

        page_index = page_number - 1 # 0, 1, 2
        word_index = CreatePDF.WORDS_PER_PAGE * page_index + word_page_index

        is_featured = word.is_featured
        linewidth = 0.6 # 1 if is_featured else 0.6
        cell.set_linewidth(linewidth)

        horizontal_align = "center"
        vertical_align = "center_baseline"

        if row_index == 0:
            # PINYIN
            height_key = "pinyin"
            facecolor = "moccasin" if is_featured else "lemonchiffon" # "gainsboro" # "whitesmoke" # "lemonchiffon"

            font_weight = 'bold'
            font_size = CreatePDF.pinyin_font_size(word_index, map_sizes)
            font_family = 'serif'

        elif row_index == 1:
            # CHINESE
            height_key = "chinese"
            facecolor = "white" # "whitesmoke"

            font_weight = 'normal'
            font_size = CreatePDF.chinese_font_size(word_index, map_sizes, word)
            # font_family = 'TC Xingkai', 'BiauKaiHK', 'Hei', 'Yuanti SC'
            font_family = 'Hiragino Sans GB'

        elif row_index == 2:
            # DEFINITIONS
            height_key = "definitions"
            facecolor = "whitesmoke"

            font_weight = 'normal'
            font_size = 8
            font_family = 'serif'
            horizontal_align = "left"
            vertical_align = 'baseline'

            text = cell.get_text()._text
            # cell_begin_x = int(row_index / 4) # 0, 1, 2, 3
            # cell_begin_y = column_index if column_index == 0 else int(column_index / 2) # 0, 1, 2, 3, 4

            # if cell_begin_x == 0 and cell_begin_y == 0:
            #     ax.text(0.1, 0.1, text, ha='left', wrap=True)

            # print("---", 0, cell_begin_y, text)
            # # print()
            # ax.text(cell_x, cell_y, text, ha='left', wrap=True)

        cell.set_facecolor(facecolor)
        cell.set_height(cls.HEIGHTS[height_key])
        # cell.set_width(0.26)

        print(font_weight,font_size,font_family)
        print(vertical_align, horizontal_align)

        cell.set_text_props(
            fontproperties=FontProperties(weight=font_weight, size=font_size, family=font_family),
            va=vertical_align,
            ha=horizontal_align
        )
        # if word_page_index > real_words_count:
                # cell.visible_edges = ''


    @classmethod
    def _page_title(cls, plt, lesson_number, page_number, total_pages, titles_dict):
        page_title = "HSK 5 - " + 'L' + str(lesson_number)
        page_title += ' - ' + titles_dict['ch']
        page_title += ' - ' + str(page_number) + "/" + str(total_pages)

        fp = FontProperties(family='Hiragino Sans GB', size=12) #, weight='bold')
        plt.suptitle(page_title, y=1.41,fontproperties=fp)


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
    def modify_cell(cls, ax, key, cell, words, real_words_count, page_number, map_sizes):
        row_index = key[0]
        column_index = key[1]
        # print(row_index, column_index)

        if row_index == 0:
            # EMPTY
            cell.set_height(cls.HEIGHTS["empty"])
            cell.visible_edges = ''

        if column_index in [1, 3, 5]:
            cell.visible_edges = ''

        elif row_index % 4 in [1, 2, 3]:
            cls._modify_cell(ax, page_number, cell, row_index, column_index, words, real_words_count, map_sizes)

        elif row_index != 0 and row_index % 4 == 0:
            # empty
            cell.set_height(cls.HEIGHTS["empty"])
            cell.visible_edges = ''


    @classmethod
    def _modify_cell(cls, ax, page_number, cell, row_index, column_index, words, real_words_count, map_sizes):
        # print(cell.get_text())
        # print(type(cell.xy))
        col_offset = int(row_index / 4) * CreatePDF.COLUMNS
        map_column = {0: 0, 2: 1, 4: 2, 6: 3}

        word_page_index = col_offset + map_column[column_index] + 1
        word_index = word_page_index + CreatePDF.WORDS_PER_PAGE * (page_number - 1) # 1, 2, ...

        is_featured = False
        word = None
        if word_index <= len(words):
            word = words[word_index - 1]
            is_featured = word.is_featured

        linewidth = 0.6 # 1 if is_featured else 0.6
        cell.set_linewidth(linewidth)

        horizontal_align = "center"
        vertical_align = "center_baseline"

        if row_index % 4 == 3:
            # DEFINITIONS
            height_key = "definitions"
            facecolor = "whitesmoke"

            font_weight = 'normal'
            font_size = 8
            font_family = 'serif'
            horizontal_align = "left"
            vertical_align = 'baseline'

            text = cell.get_text()._text
            cell_begin_x = int(row_index / 4) # 0, 1, 2, 3
            cell_begin_y = column_index if column_index == 0 else int(column_index / 2) # 0, 1, 2, 3, 4

            # if cell_begin_x == 0 and cell_begin_y == 0:
            #     ax.text(0.1, 0.1, text, ha='left', wrap=True)

            # print("---", 0, cell_begin_y, text)
            # # print()
            # ax.text(cell_x, cell_y, text, ha='left', wrap=True)

        elif row_index % 4 == 2:
            # CHINESE
            height_key = "chinese"
            facecolor = "white" # "whitesmoke"

            font_weight = 'normal'
            font_size = CreatePDF.chinese_font_size(word_index, map_sizes, word)
            # font_family = 'TC Xingkai', 'BiauKaiHK', 'Hei', 'Yuanti SC'
            font_family = 'Hiragino Sans GB'

        elif row_index % 4 == 1:
            # PINYIN
            height_key = "pinyin"
            facecolor = "moccasin" if is_featured else "lemonchiffon" # "gainsboro" # "whitesmoke" # "lemonchiffon"

            font_weight = 'bold'
            font_size = CreatePDF.pinyin_font_size(word_index, map_sizes)
            font_family = 'serif'


        cell.set_facecolor(facecolor)
        cell.set_height(cls.HEIGHTS[height_key])
        # cell.set_width(0.26)

        cell.set_text_props(
            fontproperties=FontProperties(weight=font_weight, size=font_size, family=font_family),
            va=vertical_align,
            ha=horizontal_align
        )
        if word_page_index > real_words_count:
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
