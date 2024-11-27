import sys
sys.path.append('.')

from create_pdf.hsk5_common import HSK5Common
from pypdf import PdfWriter
import os

class CreatePDFHSK5Lesson:
    OUTPUT_PATH = '/Users/pablo/Documents/CHINO/repo/confucio/create_pdf/hsk5'

    TITLES = {
        '1': {'ch': "爱的细节", 'eng': "Details of Love"},
        '2': {'ch': "留串钥匙给父母", 'eng': "Leaving a Bunch of Keys to Our Parents"},
        '3': {'ch': "人生有选择, 一切可改变", 'eng': "Having Choices in Life Makes Change Possible"},
        '4': {'ch': "子路背米", 'eng': "Zilu Carrying Rice"},
        '5': {'ch': "济南的泉水", 'eng': "Spring Water in Jinan"},
        '6': {'ch': "除夕的由来", 'eng': "Origin of Chuxi"},
        '7': {'ch': "成语故事两则", 'eng': "Two Idiom Stories"},
        '8': {'ch': '"朝三暮四"的古今义', 'eng': "Three at Dawn and Four at Dusk"},
        '9': {'ch': "别样鲁迅", 'eng': "The Lu Xun You Don't Know"},
        '10': {'ch': "争论的奇迹", 'eng': "Miracle of Debate"},
        '11': {'ch': "闹钟的危害", 'eng': "Harm of Alarm Clocks"},
        '12': {'ch': "海外用户玩儿微信", 'eng': "Overseas Users of WeChat"},
        '13': {'ch': '锯掉生活的"筐底"', 'eng': 'Cutting Off the "Bottom of the Basket" in Life'},
        '14': {'ch': "北京的四合院", 'eng': "Quadrangle Courtyards in Beijing"},
        '15': {'ch': "纸上谈兵", 'eng': "Being an Armchair Strategist"},
        '16': {'ch': "体重与节食", 'eng': "Weight and Diet"},
        '17': {'ch': "在最美好的时刻离开", 'eng': "Ending at the Best Moment"},
        '18': {'ch': "抽象艺术美不美", 'eng': "Abstract Art: Beautiful or Not?"}
    }

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

        lesson_str = '7' if lesson_number in ['7a', '7b'] else lesson_number
        titles_dict = cls.TITLES[lesson_str]

        filenames = []
        total_pages = len(word_pages)
        for idx, words_page in enumerate(word_pages):
            page_number = idx + 1
            real_words_count = len(words_page)
            filename = cls._filename(lesson_number, page_number)
            filenames.append(filename)
            HSK5Common.create_plot(
                filename, words, words_page, page_number, real_words_count, map_sizes, lesson_number, total_pages, titles_dict
            )

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
