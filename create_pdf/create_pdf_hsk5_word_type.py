import sys
sys.path.append('.')

from create_pdf.hsk5_common import HSK5Common
from classes.word_type import WordType


class CreatePDFHSK5WordType:
    @classmethod
    def generate_key(cls, word_type_key):
        words = HSK5Common.all_words()
        words = [word for word in words if ((word_type_key in word.keys()) and not word.is_featured)]
        filename_common = '/LZ-' + word_type_key + '-'
        cls.common(words, filename_common)

    @classmethod
    def generate_misc_types(cls, string):
        words = HSK5Common.all_words()
        word_type_keys = set(WordType.TYPES_HASH.keys() - ["ADV", "CLA", "PRO", "NOM", "VER", "ADJ"])
        words = [word for word in words if ((word_type_keys & set(word.keys())) and not word.is_featured)]
        filename_common = '/LZ-' + string + '-'
        cls.common(words, filename_common)

    @classmethod
    def generate_featured(cls, string):
        words = HSK5Common.all_words()
        words = [word for word in words if word.is_featured]
        filename_common = '/LZ-' + string + '-'
        cls.common(words, filename_common)

    @classmethod
    def common(cls, words, filename_common):
        if len(words) == 0:
            return

        word_pages = HSK5Common.split_words_in_pages(words)

        for idx, words_page in enumerate(word_pages):
            page_number = idx + 1

            real_words_count = len(words_page)
            data = HSK5Common.words_to_data(words_page)
            filename = filename_common + str(page_number) + '.pdf'
            HSK5Common.create_plot(data, page_number, real_words_count, filename)

CreatePDFHSK5WordType.generate_key("ADV")
CreatePDFHSK5WordType.generate_key("CLA")
CreatePDFHSK5WordType.generate_key("PRO")
CreatePDFHSK5WordType.generate_misc_types("MISC")  # TODO: fix
CreatePDFHSK5WordType.generate_featured("*****")

