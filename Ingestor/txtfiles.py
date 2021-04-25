from ..QuoteEngine import QuoteModel
from .Interface import IngestorInterface


class TextIngest(IngestorInterface):

    @classmethod
    def parse(cls, path):
        """Simple text file read"""
        file = open(path, "r", encoding="utf-8-sig")
        lines = file.readlines()
        file.close()
        """Format to have return include everything"""
        return [QuoteModel(*quote.rstrip("\n").split(" - ")) for quote in lines]
