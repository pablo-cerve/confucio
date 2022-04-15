import sys
sys.path.append('.')

import math
import os
from PIL import Image # pip3 install pillow
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, TableStyle, Table, Image as ImageDoc, PageBreak, Spacer, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, inch
from reportlab.lib.enums import TA_CENTER


class CreatePDFHSK4:
    IMAGES_PATH = "/Users/pablocerve/Documents/CHINO/HSK4/palabras"
    REPO_PATH = "/Users/pablocerve/Documents/CHINO/repo/confucio"
    FACTOR = 1.65
    IMAGES_PER_PAGE = 15
    IMAGES_PER_ROW = 3
    VERTICAL_SPACE = 0.5

    def __init__(self):
        self.image_number = 0
        self.images = []
        self.doc = None
        self.Story = []
        self.lesson_number = None

    def run(self, lesson_number):
        self.doc = self.create_doc(lesson_number)
        self.lesson_number = lesson_number
        folder_name = '/L' + str(lesson_number) + '/'
        self.run_for_folder(folder_name)
        self.doc.build(self.Story)

    def create_doc(self, lesson_number):
        top_margin = 0.5 * cm
        filename = self.IMAGES_PATH + "/pdf/L" + str(lesson_number) + ".pdf"
        doc = SimpleDocTemplate(filename, rightMargin=0.3 * cm, leftMargin=0 * cm,
                                topMargin=top_margin, bottomMargin=top_margin)
        return doc

    def run_for_folder(self, folder_name):
        images_path = self.IMAGES_PATH + folder_name
        image_filenames = sorted(os.listdir(images_path))
        image_filenames = list(filter(lambda file_name: 'DS' not in file_name, image_filenames))
        for filename in image_filenames:
            # print("filename = " + filename)
            self.image_number += 1
            # print(self.image_number)
            self.parse_image(images_path, filename)

        self.fill_last_page()

    def parse_image(self, images_path, filename):
        image_full_path = images_path + filename
        im = Image.open(image_full_path)
        assert(im.size == (320, 240))

        self.images.append(image_full_path)
        if len(self.images) != self.IMAGES_PER_ROW:
            return

        # add row
        table_data = []
        for image_full_path in self.images:
            im = ImageDoc(image_full_path, width=(4*self.FACTOR)*cm, height=(3*self.FACTOR)*cm)
            table_data.append(im)
        tbl = Table([table_data])
        self.Story.append(tbl)

        if self.image_number % self.IMAGES_PER_PAGE == 0:  # last image in current page
            print(self.image_number)
            paragraph_style = ParagraphStyle(name='Center', alignment=TA_CENTER)
            self.Story.append(Paragraph(self.footnote(), paragraph_style))
            self.Story.append(PageBreak())
        else:
            self.Story.append(Spacer(10*cm, self.VERTICAL_SPACE*cm))
        self.images = []

    def fill_last_page(self):
        if self.image_number % self.IMAGES_PER_PAGE == 0:
            return

        # Fill page using blank images (so that the page number is shown in the last page)
        remainig_images_to_complete_page = self.IMAGES_PER_PAGE - self.image_number % self.IMAGES_PER_PAGE
        for _ in range(remainig_images_to_complete_page):
            self.image_number += 1
            self.parse_blank_image()

    def parse_blank_image(self):
        self.parse_image(self.REPO_PATH + '/images/', 'BLANK.jpg')

    def footnote(self):
        lesson_str = 'L' + str(self.lesson_number)
        page_number_str = str(int(self.image_number / self.IMAGES_PER_PAGE))
        return page_number_str + ' [' + lesson_str + ']'  # 1 [L1]

# CreatePDFHSK4().run(1)
# CreatePDFHSK4().run(2)
# CreatePDFHSK4().run(3)
# CreatePDFHSK4().run(4)
# CreatePDFHSK4().run(5)
# CreatePDFHSK4().run(6)
# CreatePDFHSK4().run(7)
# CreatePDFHSK4().run(8)
# CreatePDFHSK4().run(9)
# CreatePDFHSK4().run(10)
# CreatePDFHSK4().run(11)
# CreatePDFHSK4().run(12)
# CreatePDFHSK4().run(13)
# CreatePDFHSK4().run(14)
# CreatePDFHSK4().run(15)
# CreatePDFHSK4().run(16)
# CreatePDFHSK4().run(17)
# CreatePDFHSK4().run(18)
# CreatePDFHSK4().run(19)
CreatePDFHSK4().run(20)
