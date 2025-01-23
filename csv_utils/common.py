import sys
sys.path.append('.')


class Common:
    BASE_PATH = "/Users/pablo/Documents/中文/repo/confucio"
    LESSONS_PATH = BASE_PATH + "/lessons/"

    FIRST_ROW_LESSON = ['HANZI', 'PINYIN', 'DEF1', 'TIPO1', 'DEF2', 'TIPO2', 'LECCION', 'NUM']
    FIRST_ROW_HSK1 = ['HANZI', 'PINYIN [PLECO]', 'TIPO1', 'DEF1', 'TIPO2', 'DEF2', 'LESSON', 'NUMBER', '']
    FIRST_ROW_HSK3 = ['HANZI', 'PINYIN [PLECO]', 'DEF1', 'TIPO1', 'DEF2', 'TIPO2', 'LESSON', 'NUMBER', 'LECCION', 'NUM', '#']
    FIRST_ROW_HSK4 = ['HANZI', 'PINYIN [PLECO]', 'DEF1', 'TIPO1', 'DEF2', 'TIPO2', 'LESSON', 'NUMBER', '']
    FIRST_ROW_HSK5 = FIRST_ROW_HSK1
    EXTRA_STR = "sup"

    @staticmethod
    def hsk_path(key):
        assert(key in ["hsk1"])
        hsk_path = Common.LESSONS_PATH + "/" + key
        return hsk_path

    @staticmethod
    def hsk_csv_path(key):
        hsk_csv_path = Common.hsk_path(key) + "/" + key + ".csv"
        return hsk_csv_path

    @staticmethod
    def book_path(book_number):
        return Common.LESSONS_PATH + "book" + str(book_number) + "/"

    @staticmethod
    def book_lesson_path(book_number, lesson_number, lesson_extra=False):
        filename = "lesson" + str(lesson_number) + (Common.EXTRA_STR if lesson_extra else "") + ".csv"
        return Common.book_path(book_number) + filename

    @staticmethod
    def lesson_path(lesson):
        filename = "lesson" + str(lesson.lesson_number) + (Common.EXTRA_STR if lesson.extra else "") + ".csv"
        return Common.book_path(lesson.book_number) + filename
