
from lessons.book1.lesson1 import LESSON1
from lessons.book1.lesson2 import LESSON2
from lessons.book1.lesson3 import LESSON3
from lessons.book1.lesson4 import LESSON4
from lessons.book1.lesson5 import LESSON5
from lessons.book1.lesson6 import LESSON6
from lessons.book1.lesson7 import LESSON7
from lessons.book1.lesson8 import LESSON8
from lessons.book1.lesson9 import LESSON9
from lessons.book1.lesson10 import LESSON10
from lessons.book1.lesson11 import LESSON11
from lessons.book1.lesson11_extra import LESSON11_EXTRA
from lessons.book1.lesson12 import LESSON12
from lessons.book1.lesson12_extra import LESSON12_EXTRA
from lessons.book1.lesson13 import LESSON13
from lessons.book1.lesson14 import LESSON14
from lessons.book2.lesson15 import LESSON15
from lessons.book2.lesson16 import LESSON16
from lessons.book2.lesson17 import LESSON17
from lessons.book2.lesson18 import LESSON18
from lessons.book2.lesson19 import LESSON19


class Book:
    LESSONS_1 = [LESSON1, LESSON2, LESSON3, LESSON4, LESSON5, LESSON6, LESSON7, LESSON8, LESSON9, LESSON10,
                 LESSON11, LESSON12, LESSON13, LESSON14]
    LESSONS_2 = [LESSON15, LESSON16, LESSON17, LESSON18, LESSON19]

    LESSONS_EXTRA = [None] * 10 + [LESSON11_EXTRA, LESSON12_EXTRA]

    LESSONS = LESSONS_1 + LESSONS_2

    @classmethod
    def get_lesson(cls, lesson_id, extra=False):
        if extra:
            return cls.LESSONS_EXTRA[lesson_id]
        return cls.LESSONS[lesson_id]

    @classmethod
    def book_lesson_numbers(cls, book_number):
        if book_number == 1:
            return range(1, 15)  # [1, 2, ... 14]
        if book_number == 2:
            return range(15, 19)  # [15, ... 18]
        raise ValueError("Invalid book_number: {}.".format(book_number))
