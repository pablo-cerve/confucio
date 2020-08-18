import sys
sys.path.append('.')


class Book:
    LAST_LESSON = 21

    @staticmethod
    def book_lesson_numbers(book_number):
        if book_number == 1:
            return range(1, 15)  # [1, 2, ... 14]
        if book_number == 2:
            # return range(15, 27)  # [15, ... 26]
            return range(15, Book.LAST_LESSON + 1)
        raise ValueError("Invalid book_number: {}.".format(book_number))

    @staticmethod
    def all_lesson_numbers():
        return Book.book_lesson_numbers(1) + Book.book_lesson_numbers(2)

    @staticmethod
    def book_number(lesson_number):
        if 1 <= lesson_number <= 14:
            return 1
        if 15 <= lesson_number <= 26:
            return 2
        raise ValueError("Invalid lesson_number: {}.".format(lesson_number))
