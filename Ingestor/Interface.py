"""Determine what type of file it is"""

ext = {
     "Text": ".txt",
     "CSV": ".csv",
     "PDF": ".pdf",
     "docx": ".docx",
}

"""Ingestor Class for verification and parse with use of extensions dictionary"""


class IngestorInterface:

    @classmethod
    def verification(cls, file_ext):
        return file_ext in ext.values()

    @classmethod
    def parse(cls, path):
        pass
