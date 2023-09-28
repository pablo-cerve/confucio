import sys
sys.path.append('.')

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
        4: {},
        5: {
            8:  {'chinese': 3},
            36: {'chinese': 3},
            42: {'chinese': 3, 'pinyin': 11},
            49: {'chinese': 4, 'pinyin': 9},
            50: {'chinese': 3}
        },
        6: {
            24: {'chinese': 3}
        }
    }

    @classmethod
    def generate(cls, lesson_number):
        map_sizes = cls.MAP_SIZES[lesson_number]
        words = HSK5Common.lesson_words(lesson_number)
        word_pages = HSK5Common.split_words_in_pages(words)
        filename_common = '/L' + str(lesson_number) + '-'

        for idx, words_page in enumerate(word_pages):
            page_number = idx + 1

            real_words_count = len(words_page)
            data = HSK5Common.words_to_data(words_page)
            filename = filename_common + str(page_number) + '.pdf'
            HSK5Common.create_plot(data, page_number, real_words_count, filename, map_sizes)


# CreatePDFHSK5Lesson.generate(1)
# CreatePDFHSK5Lesson.generate(2)
# CreatePDFHSK5Lesson.generate(3)
# CreatePDFHSK5Lesson.generate(4)
# CreatePDFHSK5Lesson.generate(5)
CreatePDFHSK5Lesson.generate(6)
