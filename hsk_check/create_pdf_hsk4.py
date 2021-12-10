import sys
sys.path.append('.')

import math
import os
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, TableStyle, Table, Image as ImageDoc, PageBreak, Spacer, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, inch
from reportlab.lib.enums import TA_CENTER


class CreatePDFHSK4:
    IMAGES_PATH = "/Users/pablocerve/Documents/CHINO/HSK4/palabras"
    FACTOR = 1.65
    IMAGES_PER_PAGE = 15
    IMAGES_PER_ROW = 3
    VERTICAL_SPACE = 0.5

    def __init__(self):
        self.image_number = 0
        self.images = []
        self.doc = self.create_doc()
        self.Story = []

    def create_doc(self):
        top_margin = 0.5 * cm
        filename = self.IMAGES_PATH + "/file.pdf"
        doc = SimpleDocTemplate(filename, rightMargin=0.3 * cm, leftMargin=0 * cm,
                                topMargin=top_margin, bottomMargin=top_margin)
        return doc

    def run(self):
        for number in range(1, 2):
            folder_name = '/L' + str(number) + '/'
            self.run_for_folder(folder_name)
        self.doc.build(self.Story)

    def run_for_folder(self, folder_name):
        images_path = self.IMAGES_PATH + folder_name
        for filename in sorted(os.listdir(images_path)):
            if 'DS' in filename:
                continue
            # print("filename = " + filename)
            self.image_number += 1
            # print(self.image_number)
            self.parse_image(images_path, filename)

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

        if self.image_number % self.IMAGES_PER_PAGE == 0:
            print(self.image_number)
            page_number = str(int(self.image_number / 15))
            paragraph_style = ParagraphStyle(name='Center', alignment=TA_CENTER)
            self.Story.append(Paragraph(page_number, paragraph_style))
            self.Story.append(PageBreak())
        else:
            self.Story.append(Spacer(10*cm, self.VERTICAL_SPACE*cm))
        self.images = []

CreatePDFHSK4().run()
