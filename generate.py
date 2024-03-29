
from classes.lesson import Lesson
from csv_utils.writer import Writer
from csv_utils.common import Common
from classes.book import Book


def print_lessons(filename, lesson_numbers, word_keys=None):
    path = Common.GENERATED_PATH + filename
    lessons = []
    for lesson_number in lesson_numbers:
        lesson_number = int(lesson_number) if lesson_number[0] == "0" in lesson_number else lesson_number
        lesson = Lesson(lesson_number)
        lessons.append(lesson)
    Writer.write_lessons(path, lessons, word_keys)


print_lessons("libro1.csv", Book.book_lesson_numbers(1))
print_lessons("libro2.csv", Book.book_lesson_numbers(2))
print_lessons("palabras-l1-a-l24.csv", Book.all_lesson_numbers())

print_lessons("verbos.csv", Book.all_lesson_numbers(), ['VER'])
print_lessons("adverbios.csv", Book.all_lesson_numbers(), ['ADV'])
print_lessons("adjetivos.csv", Book.all_lesson_numbers(), ['ADJ'])
