import sys
sys.path.append('.')


class Common:
    LESSONS_PATH = "/Users/pablocerve/Documents/CHINO/repo/confucio/lessons"
    FIRST_ROW = ['HANZI', 'PINYIN', 'DEF1', 'TIPO1', 'DEF2', 'TIPO2', 'LECCION']

    @staticmethod
    def book_lesson_path(book_number, lesson_id, lesson_extra=False):
        path = Common.LESSONS_PATH + "/book" + str(book_number) + "/"
        filename = "lesson" + str(lesson_id) + ("_extra" if lesson_extra else "") + ".csv"
        return path + filename

    @staticmethod
    def lesson_path(lesson):
        path = Common.LESSONS_PATH + "/book" + str(lesson.book_number) + "/"
        filename = "lesson" + str(lesson.lesson_id) + ("_extra" if lesson.extra else "") + ".csv"
        return path + filename
