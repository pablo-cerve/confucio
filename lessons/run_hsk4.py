import sys
sys.path.append('.')

from csv_utils.reader import Reader
from csv_utils.common import Common
from classes.printer import Printer
# from hsk_check.hsk_check import HSKCheck

# HSKCheck.compare_with_official()
# HSKCheck.compare_with_images()

path = Common.HSK4_PATH + "hsk4.csv"
reader = Reader(path, 'hsk4')
words = reader.generate_words()
Printer.print_definition_hsk4(words)
