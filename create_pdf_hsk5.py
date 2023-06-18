import sys
sys.path.append('.')

import numpy as np
import matplotlib
matplotlib.rcParams['font.family'] = ['Heiti TC']

import matplotlib.pyplot as plt
from csv_utils.common import Common
from csv_utils.reader import Reader
from reportlab.platypus import SimpleDocTemplate, TableStyle, Table, Image as ImageDoc, PageBreak, Spacer, Paragraph
from reportlab.lib.units import cm, inch


class CreatePDFHSK5:
    INPUT_PATH = '/Users/pablocerve/Documents/CHINO/repo/confucio/lessons/hsk5'
    INPUT_FILE = 'hsk5.csv'
    OUTPUT_PATH = '/Users/pablocerve/Documents/CHINO/HSK5/palabras'
    ROWS = 6
    COLUMNS = 4

    def __init__(self):
        # self.doc = self.create_doc()
        pass

    def run(self, lesson_number):
        # words = self.lesson_words(lesson_number)
        # data = self.words_to_data(words)
        self.create_plot(lesson_number)

    def lesson_words(self, lesson_number):
        path = Common.HSK5_PATH + "hsk5.csv"
        reader = Reader(path, 'hsk5')
        words = reader.generate_words()
        filtered_words = [word for word in words if word.lesson_number == lesson_number]
        return filtered_words

    def words_to_data(self, ax, words):
        data = []
        current_page = []
        current_row = []
        for word in words:
            current_row.append(word)
            if len(current_row) == self.COLUMNS:
                empty_row = [None for _ in current_row]
                chinese_row = [word.chinese for word in current_row]
                pinyin_row = [word.pinyin.lower() for word in current_row]
                current_page.append(empty_row)
                current_page.append(chinese_row)
                current_page.append(pinyin_row)
                current_row = []
                if len(current_page) == self.ROWS:
                    data.append(current_page)
                    current_page = []
        if len(current_row) > 0:
            empty_row = [None for _ in current_row]
            chinese_row = [word.chinese for word in current_row]
            pinyin_row = [word.chinese.lower() for word in current_row]
            current_page.append(empty_row)
            current_page.append(chinese_row)
            current_page.append(pinyin_row)
        if len(current_page) > 0:
            data.append(current_page)
        return data


    def create_plot(self, lesson_number):
        fig, ax = plt.subplots()

        words = self.lesson_words(lesson_number)
        data = self.words_to_data(ax, words)

        # Hide axes
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)

        colWidths = [0.25] * self.COLUMNS
        table = ax.table(cellText=data[0],loc='center', cellLoc='center', colWidths=colWidths)
        table.auto_set_font_size(False)
        # table.set_fontsize(25)
        # table.scale(1, 4)

        for key, cell in table.get_celld().items():
            print(key)
            print(cell)
            if key[0] % 3 == 0:
                cell.set_height(.1)
                cell.visible_edges = 'TB'
                # cell.set_linewidth(0)
            elif key[0] % 3 == 1:
                print("B")
                cell.set_height(.3)
                cell.set_fontsize(40)
            elif key[0] % 3 == 2:
                # cell.set_linewidth(2)
                cell.set_height(.1)
                cell.set_fontsize(12)

        #     if key[0] % 2 == 0:
        #       print("A")
        #       cell.set_linewidth(0)
        #       cell.set_fontsize(10)
        #     else:
        #       print("B")
        #       cell.set_fontsize(50)
        #     # scrub borders for clean look(see source below)
        #     # cell.set_linewidth(0)
        #
        #     # adjust format for only header col and row to help with space issues
        #     # col header on 0, row header on -1.
        #     # if key[0] == 0 or key[1] == -1:
        #     #     cell.set_fontsize(6)

        plt.show()



    # def add_word(self, idx, word):
    #     print(word.lesson_number)
    #     print(word.pinyin)
    #     print(word.chinese)
    #     print(word.chinese_l)







# CreatePDFHSK5().run(1)
# CreatePDFHSK5().run(2)
# CreatePDFHSK5().run(3)
CreatePDFHSK5().run(4)