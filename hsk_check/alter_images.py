import sys
sys.path.append('.')

import math
import os
from PIL import Image


class AlterImages:
    IMAGES_PATH = "/Users/pablo/Documents/CHINO/HSK3/palabras/oficiales"

    @classmethod
    def reduce_images_size(cls):
        cls.reduce_images_size_folder('/001-100/')
        cls.reduce_images_size_folder('/001-100/')
        cls.reduce_images_size_folder('/101-200/')
        cls.reduce_images_size_folder('/201-300/')
        cls.reduce_images_size_folder('/301-400/')
        cls.reduce_images_size_folder('/401-500/')
        cls.reduce_images_size_folder('/501-600/')

    @classmethod
    def change_images_names(cls):
        cls.change_images_names_folder('/001-100/', 1)
        cls.change_images_names_folder('/101-200/', 101)
        cls.change_images_names_folder('/201-300/', 201)
        cls.change_images_names_folder('/301-400/', 301)
        cls.change_images_names_folder('/401-500/', 401)
        cls.change_images_names_folder('/501-600/', 501)

    ######################################################################

    @classmethod
    def reduce_images_size_folder(cls, folder_name):
        images_path = cls.IMAGES_PATH + folder_name
        for filename in sorted(os.listdir(images_path)):
            if 'DS' in filename:
                continue
            print(filename)
            im = Image.open(images_path + filename)
            if im.size == (256, 192):
                continue
            assert(im.size == (320, 240))
            # filters = [Image.NEAREST, Image.BILINEAR, Image.BICUBIC,  Image.ANTIALIAS]
            im.thumbnail((256, 192), Image.BILINEAR)
            im.save(images_path + filename, "JPEG", quality=100)

    @classmethod
    def change_images_names_folder(cls, folder_name, number_start):
        images_path = cls.IMAGES_PATH + folder_name
        current_n = number_start

        for filename in sorted(os.listdir(images_path)):
            if 'DS' in filename:
                continue
            new_filename = cls.new_filename(current_n, filename)
            print(current_n, new_filename)
            os.rename(images_path + filename, images_path + new_filename)
            current_n += 1

    @classmethod
    def new_filename(cls, number, filename):
        str_number = str(number)
        if number < 10:
            str_number = '00' + str_number
        elif number < 100:
            str_number = '0' + str_number
        after_number = filename[3]
        assert(after_number in ['-', 'a', 'b'])
        index = 3 if after_number == '-' else 4
        return str_number + filename[index:]


# AlterImages.reduce_images_size()
AlterImages.change_images_names()
