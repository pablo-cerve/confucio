
from classes.lesson import Lesson
from csv_utils.reader import Reader
from csv_utils.writer import Writer

# Writer(1, 1, Lesson(1)).save_csv()
Writer(1, 1, Reader(1, 1).generate_lesson()).save_csv()



# lesson = Lesson(1).print_definition()
# Reader(2, 20).generate_lesson()

# lesson = Lesson(2).print_definition()
# lesson = Lesson(3).print_definition()
# lesson = Lesson(4).print_definition()
# lesson = Lesson(5).print_definition()
# lesson = Lesson(6).print_definition()
# lesson = Lesson(7).print_definition()
# lesson = Lesson(8).print_definition()
# lesson = Lesson(9).print_definition()
# lesson = Lesson(10).print_definition()
# lesson = Lesson(11).print_definition()
# lesson = Lesson(11, True).print_definition()
# lesson = Lesson(12).print_definition()
# lesson = Lesson(12, True).print_definition()
# lesson = Lesson(13).print_definition()
# lesson = Lesson(14).print_definition()
# lesson = Lesson(15).print_definition()
# lesson = Lesson(16).print_definition()
# lesson = Lesson(17).print_definition()
# lesson = Lesson(18).print_definition()
# lesson = Lesson(19).print_definition()
# lesson = Lesson(19).print_definition()
# Reader(2, 20).generate_lesson().print_definition()

# lesson.print_all()
# lesson.print_pinyin()
# lesson.print_chinese()
# lesson.print_definition()
