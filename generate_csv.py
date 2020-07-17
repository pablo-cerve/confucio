
from csv_utils.reader import Reader
from csv_utils.writer import Writer
from csv_utils.common import Common

# extra = [11, 12]
# for lesson_number in range(1, 20):
#     # Writer.write_lesson(Lesson(lesson_number))
#     Writer.write_lesson(Reader(lesson_number).generate_lesson())
#
#     if lesson_number in extra:
#         # Writer.write_lesson(Lesson(lesson_number, True))
#         Writer.write_lesson(Reader(lesson_number).generate_lesson())
#
# Writer.write_lesson(Reader(20).generate_lesson())


def print_book(book_number):
    path = Common.book_path(book_number) + "book" + str(book_number) + ".csv"
    lesson_range = range(1, 15) if book_number == 1 else range(15, 21)
    lessons = []
    for lesson_number in lesson_range:
        lesson = Reader(lesson_number).generate_lesson()
        lessons.append(lesson)
    Writer.write_lessons(path, lessons)

print_book(1)
print_book(2)
