
from pypdf import PdfWriter
import os

class CreatePDFUtils:
    @classmethod
    def merge_pdfs(cls, pdf_paths, new_pdf_path):
        cls._merge_pdfs(pdf_paths, new_pdf_path)
        cls._remove_pdfs(pdf_paths)


    @classmethod
    def _merge_pdfs(cls, pdf_paths, new_pdf_path):
        merger = PdfWriter()
        for pdf_path in pdf_paths:
            merger.append(pdf_path)

        merger.write(new_pdf_path)
        merger.close()


    @classmethod
    def _remove_pdfs(cls, pdf_paths):
        for pdf_path in pdf_paths:
            os.remove(pdf_path)
