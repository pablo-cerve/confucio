
from lesson1 import LESSON1
from lesson2 import LESSON2
from lesson3 import LESSON3
from lesson4 import LESSON4
from lesson5 import LESSON5
from lesson6 import LESSON6
# from lesson6 import LESSON7
# from lesson6 import LESSON8
# from lesson6 import LESSON10
# from lesson6 import LESSON11

LESSONS = [LESSON1, LESSON2, LESSON3, LESSON4, LESSON5, LESSON6]  # , LESSON7, LESSON8, LESSON9, LESSON10, LESSON11]


def get_lesson(lesson_id):
    return LESSONS[lesson_id]
