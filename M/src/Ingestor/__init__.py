import os

"""Import all ingestors"""
from .Interface import IngestorInterface, ext
from .csvfiles import CSVIngest
from .pdffiles import PDFIngest
from .txtfiles import TextIngest
from .docxfiles import DocxIngest


class Ingestor(IngestorInterface):

    """Check for file extensions using get then return into respective extension function from imports"""
    @classmethod
    def parse(cls, path):
        filename, file_ext = os.path.splitext(path)
        if not cls.verification(file_ext):
            raise ValueError("File extension not supported:", file_ext)
        if file_ext == ext.get("CSV"):
            return CSVIngest.parse(path)
        if file_ext == ext.get("PDF"):
            return PDFIngest.parse(path)
        if file_ext == ext.get("Text"):
            return TextIngest.parse
        if file_ext == ext.get("docx"):
            return DocxIngest.parse(path)
