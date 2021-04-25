import os
import subprocess

from .Interface import IngestorInterface
from .txtfiles import TextIngest


class PDFIngest(IngestorInterface):
    @classmethod
    def parse(cls, path):
        text = './pdf_to_text.txt'
        """Format"""
        lay = f"./pdftotext -layout -nopgbrk {path} {text}"
        """Subprocess call to get return value"""
        subprocess.call(lay, shell=True, stderr=subprocess.STDOUT)
        """Use TextIngest function """
        quote = TextIngest.parse(text)
        os.remove(text)
        return quote
