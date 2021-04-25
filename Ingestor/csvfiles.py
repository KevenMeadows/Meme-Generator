import pandas as pan

from ..QuoteEngine import QuoteModel
from .Interface import IngestorInterface


class CSVIngest(IngestorInterface):

    @classmethod
    def parse(cls, path):
        """Use pandas to convert csv easily"""
        csv = pan.read_csv(path)
        """Format to have return go through each row"""
        return [QuoteModel(**row) for index, row in csv.iterrows()]
