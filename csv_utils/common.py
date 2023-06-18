import sys
sys.path.append('.')


class Common:
    LESSONS_PATH = "/Users/pablocerve/Documents/CHINO/repo/confucio/lessons/"
    HSK3_PATH = LESSONS_PATH + "hsk3/"
    HSK4_PATH = LESSONS_PATH + "hsk4/"
    HSK5_PATH = LESSONS_PATH + "hsk5/"
    GENERATED_PATH = LESSONS_PATH + "generated/"
    FIRST_ROW_LESSON = ['HANZI', 'PINYIN', 'DEF1', 'TIPO1', 'DEF2', 'TIPO2', 'LECCION', 'NUM']
    FIRST_ROW_HSK3 = ['HANZI', 'PINYIN [PLECO]', 'DEF1', 'TIPO1', 'DEF2', 'TIPO2', 'LESSON', 'NUMBER', 'LECCION', 'NUM', '#']
    FIRST_ROW_HSK4 = ['HANZI', 'PINYIN [PLECO]', 'DEF1', 'TIPO1', 'DEF2', 'TIPO2', 'LESSON', 'NUMBER', '']
    EXTRA_STR = "sup"

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
