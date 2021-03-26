import csv
from file_utils.auxi import full_path


class CSVReader:
    def __init__(self, path, filename, delimiter=','):
        self.path, self.filename = path, filename
        self.full_path = full_path(path, filename)
        self.file = self.open_file()
        self.csv_reader = csv.reader(self.file, delimiter=delimiter)
        self.total_lines = self.total_lines_()
        self.continue_reading = True
        self.current_line_count = 0
        self.previous_row = next(self.csv_reader, None)

    @classmethod
    def first_data_row(cls, path, filename):
        csv_reader = CSVReader(path, filename)
        last_header_row = 1
        while csv_reader.continue_reading:
            line = csv_reader.read_line()
            if line[0] == "DATA:":
                break
            last_header_row += 1
        csv_reader.close()
        return last_header_row

    def goto_row(self, row_number):
        if row_number >= self.total_lines:
            raise(StandardError, "PRE: row_number < self.total_lines failed.")
        self.file.seek(0)  # https://stackoverflow.com/a/431771/4547232
        self.continue_reading = True
        self.current_line_count = 0
        self.previous_row = next(self.csv_reader, None)
        for _ in range(row_number):
            self.read_line()

    def goto_first_data_row(self):
        first_data_row = self.first_data_row(self.path, self.filename)
        self.goto_row(first_data_row + 1)

    # PRE: self.continue_reading
    def read_line(self):
        previous_row = self.previous_row
        row = next(self.csv_reader, None)
        if not row:
            self.continue_reading = False
        else:
            self.current_line_count += 1
            self.previous_row = row

        return previous_row

    def total_lines_(self):
        # print(self.full_path)
        return sum(1 for _ in csv.reader(self.open_file()))

    def open_file(self):
        return open(self.full_path, "r")
        # if OSUtils.ubuntu():
        #     return open(self.full_path, "rU", "utf-16")
        # else:
        #     return open(self.full_path, "r")

    def close(self):
        self.file.close()
