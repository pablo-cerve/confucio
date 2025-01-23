
from create_pdf.create_pdf import CreatePDF
from create_pdf.create_pdf_utils import CreatePDFUtils


class CreatePDFHSK1All:
    @classmethod
    def generate(cls, base_path):
        path = base_path + "/lessons/hsk1/"
        new_pdf_path = path + "HSK1.pdf"

        pdf_paths = cls._create_individual_pdfs(path)

        CreatePDFUtils.merge_pdfs(pdf_paths, new_pdf_path)

    @classmethod
    def _create_individual_pdfs(cls, path):
        words = CreatePDF.words('hsk1')
        sss
        return words