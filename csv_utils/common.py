import sys
sys.path.append('.')


class Common:
    LESSONS_PATH = "/Users/pablocerve/Documents/CHINO/repo/confucio/lessons/"
    GENERATED_PATH = LESSONS_PATH + "generated/"
    FIRST_ROW = ['HANZI', 'PINYIN', 'DEF1', 'TIPO1', 'DEF2', 'TIPO2', 'LECCION', 'NUM']
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
