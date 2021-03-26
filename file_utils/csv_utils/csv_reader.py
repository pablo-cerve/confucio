import csv
from file_utils.auxi import full_path


class CSVReader:
    def __init__(self, path, filename, delimiter=','):
        self.lines = []
        with open(path + '/' + filename, encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter)
            for line in reader:
                self.lines.append(line)
