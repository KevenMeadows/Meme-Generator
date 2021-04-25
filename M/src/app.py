import random
import os

import requests
from flask import Flask, render_template, abort, request

# @TODO Import your Ingestor and MemeEngine classes
from Ingestor import Ingestor
from MemeEngine.Meme_Engine import MemeEngine

app = Flask(__name__)


meme = MemeEngine('./static')


def setup():
    """ Load all resources """
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    """Very similar implementation as meme file code"""
    """Variable for all quotes"""
    """For loop with try except calling Ingestor class parse"""
    """ to add quotes you need array"""
    quote = []
    for i in quote_files:
        try:
            quote.extend(Ingestor.parse(i))
        except ValueError as error:
            print(f"ValueError: {error}")

    images_path = "./_data/photos/dog/"
    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    """For all images"""
    image = []
    """For loop similar to meme.py applies format to image file to pull it"""
    for root, dirs, files in os.walk(images_path):
        image = [os.path.join(root, name) for name in files]
    return quote, image


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array
    """Random choice using returned imgs array"""
    img = random.choice(imgs)
    """Random choice using returned quotes array"""
    quote = random.choice(quotes)
    """Change meme.make_meme to fit my code"""
    path = meme.format_and_make(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.
    """Set temp"""
    img = "./temp_image.jpeg"
    """Use imported request lib to retrieve attributes"""
    image_url = request.form.get("image_url")
    image_data = requests.get(image_url, stream=True).content
    """wb used to write jpeg"""
    with open(img, "wb") as file:
        file.write(image_data)
    """Use imported request lib to retrieve attributes"""
    body = request.form.get("body", "")
    author = request.form.get("body", "")
    path = meme.format_and_make(img, body, author)
    print(path)
    """Remove temp img"""
    os.remove(img)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
