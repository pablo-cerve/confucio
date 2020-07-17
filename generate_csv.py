
from classes.lesson import Lesson
from csv_utils.reader import Reader
from csv_utils.writer import Writer

# Writer(1, 1, Lesson(1)).save_csv()
# Writer(1, 1, Reader(1, 1).generate_lesson()).save_csv()

extra = [11, 12]

for lesson_number in range(1, 20):
    Writer.write_lesson(Lesson(lesson_number))
    if lesson_number in extra:
        Writer.write_lesson(Lesson(lesson_number, True))


Writer.write_lesson(Reader(20).generate_lesson())
