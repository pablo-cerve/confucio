
from classes.lesson import Lesson
from csv_utils.writer import Writer
from csv_utils.common import Common
from classes.book import Book


def print_lessons(filename, lesson_numbers):
    path = Common.GENERATED_PATH + filename
    lessons = []
    for lesson_number in lesson_numbers:
        lesson = Lesson(lesson_number)
        lessons.append(lesson)
    Writer.write_lessons(path, lessons)


print_lessons("book_1.csv", Book.book_lesson_numbers(1))
print_lessons("book_2.csv", Book.book_lesson_numbers(2))
print_lessons("book_complete.csv", Book.all_lesson_numbers())
