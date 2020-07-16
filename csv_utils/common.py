import sys
sys.path.append('.')


class Common:
    LESSONS_PATH = "/Users/pablocerve/Documents/CHINO/repo/confucio/lessons"
    FIRST_ROW = ['HANZI', 'PINYIN', 'DEF1', 'TIPO1', 'DEF2', 'TIPO2']

    @staticmethod
    def lesson_path(book_number, lesson_number):
        return Common.LESSONS_PATH + "/book" + str(book_number) + "/lesson" + str(lesson_number)
