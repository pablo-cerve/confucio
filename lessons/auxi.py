
from lesson1 import LESSON1
from lesson2 import LESSON2
from lesson3 import LESSON3
from lesson4 import LESSON4
from lesson5 import LESSON5
from lesson6 import LESSON6
from lesson7 import LESSON7
from lesson8 import LESSON8
from lesson9 import LESSON9
from lesson10 import LESSON10
from lesson11 import LESSON11
from lesson11_extra import LESSON11_EXTRA
from lesson12 import LESSON12
from lesson12_extra import LESSON12_EXTRA
from lesson13 import LESSON13
from lesson14 import LESSON14
from lesson15 import LESSON15
from lesson16 import LESSON16
from lesson17 import LESSON17


LESSONS = [LESSON1, LESSON2, LESSON3, LESSON4, LESSON5, LESSON6, LESSON7, LESSON8, LESSON9, LESSON10,
           LESSON11, LESSON12, LESSON13, LESSON14, LESSON15, LESSON16, LESSON17]
LESSONS_EXTRA = [None] * 10 + [LESSON11_EXTRA, LESSON12_EXTRA]


def get_lesson(lesson_id, extra=False):
    if extra:
        return LESSONS_EXTRA[lesson_id]
    return LESSONS[lesson_id]
