
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


LESSONS = [LESSON1, LESSON2, LESSON3, LESSON4, LESSON5, LESSON6, LESSON7, LESSON8, LESSON9, LESSON10,
           LESSON11, LESSON12, LESSON13, LESSON14, LESSON15, LESSON16, LESSON17, LESSON18]
LESSONS_EXTRA = [None] * 10 + [LESSON11_EXTRA, LESSON12_EXTRA]


def get_lesson(lesson_id, extra=False):
    if extra:
        return LESSONS_EXTRA[lesson_id]
    return LESSONS[lesson_id]
