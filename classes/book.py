import sys
sys.path.append('.')


class Book:
    @staticmethod
    def book_lesson_numbers(book_number):
        if book_number == 1:
            return range(1, 15)  # [1, 2, ... 14]
        if book_number == 2:
            return range(15, 27)  # [15, ... 26]
        raise ValueError("Invalid book_number: {}.".format(book_number))

    @staticmethod
    def book_number(lesson_number):
        if 1 <= lesson_number <= 14:
            return 1
        if 15 <= lesson_number <= 26:
            return 2
        raise ValueError("Invalid lesson_number: {}.".format(lesson_number))
