from docx import Document

from ..QuoteEngine import QuoteModel
from .Interface import IngestorInterface


class DocxIngest(IngestorInterface):
    @classmethod
    def parse(cls, path):
        """Use docx Document import to convert"""
        doc = Document(path)
        quote = []
        """For loop that appends text for easier return"""
        for para in doc.paragraphs:
            para.text and quote.append(QuoteModel(*para.text.split(" - ")))
        return quote