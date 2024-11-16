import sys
sys.path.append('.')

from create_pdf.hsk5_common import HSK5Common
from pypdf import PdfWriter
import os

class CreatePDFHSK5Lesson:
    OUTPUT_PATH = '/Users/pablo/Documents/CHINO/repo/confucio/create_pdf/hsk5'

    # 11, 10, 9.5, 9, 8.5
    MAP_SIZES = {
        '1': {
            15: {'pinyin': 10}, # no 11
            24: {'pinyin': 11},
            38: {'pinyin': 9.5} # no 10
        },
        '5': {
            42: {'pinyin': 11},
            49: {'pinyin': 9}, # no 9.5
        },
        '7b': {
            1: {'chinese': 4.5, 'pinyin': 9}, # no 9.5
            2: {'pinyin': 9}, # no 9.5
            14: {'pinyin': 8.5} # no 9
        },
        '9': {
            25: {'pinyin': 9.5}, # no 10
            44: {'chinese': 3},
            45: {'chinese': 3}
        },
        '10': {
            38: {'pinyin': 10}
        },
        '11': {
            42: {'pinyin': 10},
            43: {'pinyin': 11},
            44: {'pinyin': 9}
        },
        '12': {
            48: {'pinyin': 10}
        }
    }

    @classmethod
    def generate(cls, lesson_number):
        lesson_number = str(lesson_number)
        filenames = cls._create_individual_pdfs(lesson_number)
        cls._merge_pdfs(filenames, lesson_number)
        cls._remove_pdfs(filenames)

    @classmethod
    def _create_individual_pdfs(cls, lesson_number):
        map_sizes = cls.MAP_SIZES.get(lesson_number, {})
        words = HSK5Common.lesson_words(lesson_number)
        word_pages = HSK5Common.split_words_in_pages(words)

        filenames = []
        total_pages = len(word_pages)
        for idx, words_page in enumerate(word_pages):
            page_number = idx + 1
            real_words_count = len(words_page)
            filename = cls._filename(lesson_number, page_number)
            filenames.append(filename)
            HSK5Common.create_plot(filename, words, words_page, page_number, real_words_count, map_sizes, lesson_number, total_pages)

        return filenames

    @classmethod
    def _filename(cls, lesson_number, page_number):
        filename = 'L' + str(lesson_number) + '-' + str(page_number) + '.pdf'
        filename = cls.OUTPUT_PATH + "/" + filename
        return filename

    @classmethod
    def _merge_pdfs(cls, filenames, lesson_number):
        merger = PdfWriter()
        for filename in filenames:
            merger.append(filename)

        filename = 'L' + str(lesson_number) + '.pdf'
        filename = cls.OUTPUT_PATH + "/" + filename
        merger.write(filename)
        merger.close()

    @classmethod
    def _remove_pdfs(cls, filenames):
        for filename in filenames:
            os.remove(filename)
