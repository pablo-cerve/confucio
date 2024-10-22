import sys
sys.path.append('.')

from create_pdf.hsk5_common import HSK5Common


class CreatePDFHSK5Lesson:
    MAP_SIZES = {
        '1': {
            15: {'chinese': 4, 'pinyin': 10},
            18: {'chinese': 3},
            24: {'chinese': 4, 'pinyin': 11},
            38: {'chinese': 4, 'pinyin': 9}
        },
        '2': {
            2:  {'chinese': 3},
            16: {'chinese': 3}
        },
        '3': {
            24: {'chinese': 3},
            43: {'chinese': 4},
            44: {'chinese': 3}
        },
        '4': {},
        '5': {
            8:  {'chinese': 3},
            36: {'chinese': 3},
            42: {'chinese': 3, 'pinyin': 11},
            49: {'chinese': 4, 'pinyin': 9},
            50: {'chinese': 3}
        },
        '6': {
            24: {'chinese': 3}
        },
        '7a': {},
        '7b': {
            1: {'chinese': 5, 'pinyin': 9},
            2: {'chinese': 5, 'pinyin': 9},
            10: {'chinese': 3},
            14: {'chinese': 4, 'pinyin': 8.5}
        },
        '8': {
            1: {'chinese': 4},
            8: {'chinese': 3}
        }
    }

    @classmethod
    def generate(cls, lesson_number):
        lesson_number = str(lesson_number)
        map_sizes = cls.MAP_SIZES[lesson_number]
        words = HSK5Common.lesson_words(lesson_number)
        word_pages = HSK5Common.split_words_in_pages(words)

        total_pages = len(word_pages)
        for idx, words_page in enumerate(word_pages):
            page_number = idx + 1
            real_words_count = len(words_page)
            HSK5Common.create_plot(words_page, page_number, real_words_count, map_sizes, lesson_number, total_pages)
