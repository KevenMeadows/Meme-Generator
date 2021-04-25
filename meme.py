import os
import random
"""Import ArgumentParser for later use"""
from argparse import ArgumentParser

# @TODO Import your Ingestor and MemeEngine classes
from Ingestor import Ingestor
from QuoteEngine import QuoteModel
from MemeEngine.Meme_Engine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    """Not used error?"""
    """img = None """
    """Not used error?"""
    """quote = None"""
    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    """Changed meme.make_meme to fit my coded function"""
    path = meme.format_and_make(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # @TODO Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    """Standard help message"""
    parser = ArgumentParser(description="Generate meme and print path.")
    """Help message for path"""
    parser.add_argument("--path", type=str, required=False, nargs="?", default=None, help="path to image")
    """Help message for body"""
    parser.add_argument("--body", type=str, required=False, nargs="?", default=None, help="quote body")
    """Help message for author"""
    parser.add_argument("--author", type=str, required=False, nargs="?", default=None, help="quote author")
    """Change from None to establish parser arg"""
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
