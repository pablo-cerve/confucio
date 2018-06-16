
from lesson1 import LESSON1
from lesson2 import LESSON2
from lesson3 import LESSON3
from lesson4 import LESSON4
from lesson5 import LESSON5
# from lesson6 import LESSON6

LESSONS = [LESSON1, LESSON2, LESSON3, LESSON4, LESSON5]  # , LESSON6]


def get_lesson(lesson_id):
    return LESSONS[lesson_id]
