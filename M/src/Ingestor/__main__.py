from ..Ingestor import Ingestor

quotes = {'./_data/DogQuotes/DogQuotesTXT.txt',
          './_data/DogQuotes/DogQuotesDOCX.docx',
          './_data/DogQuotes/DogQuotesPDF.pdf',
          './_data/DogQuotes/DogQuotesCSV.csv'
          }
"""For loop to check for errors and let user know if error occurred"""
for x in quotes:
    try:
        print(Ingestor.parse(x))
    except ValueError as error:
        print(f"Value Error: {error}")
