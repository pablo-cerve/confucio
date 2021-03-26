import sys
sys.path.append('.')


class Book:
    LAST_LESSON = 24
    EXTRA_LESSONS = {
        1: [11, 12],
        2: [20, 22, 23]
    }
    EXTRA_STR = "sup"

    @staticmethod
    def book_lesson_numbers(book_number, include_extra=True):
        if book_number == 1:
            numbers = range(1, 15)  # [1, 2, ... 14]
        elif book_number == 2:
            numbers = range(15, Book.LAST_LESSON + 1)  # [15, ... Book.LAST_LESSON]
        else:
            raise ValueError("Invalid book_number: {}.".format(book_number))
        numbers = ["0" + str(number) if number < 10 else str(number) for number in numbers]
        return numbers if not include_extra else Book.add_extra(book_number, numbers)

    @staticmethod
    def add_extra(book_number, numbers):
        extra_lessons = [str(number) + Book.EXTRA_STR for number in Book.EXTRA_LESSONS[book_number]]
        numbers += extra_lessons
        numbers.sort()
        print(numbers)
        return numbers

    @staticmethod
    def all_lesson_numbers():
        return Book.book_lesson_numbers(1) + Book.book_lesson_numbers(2)

    @staticmethod
    def book_number(lesson_number):
        if isinstance(lesson_number, basestring):
            lesson_number = lesson_number.replace(Book.EXTRA_STR, "")
            lesson_number = int(lesson_number)
        if 1 <= lesson_number <= 14:
            return 1
        if 15 <= lesson_number <= 26:
            return 2
        raise ValueError("Invalid lesson_number: {}.".format(lesson_number))
