# Meme Generator Project

Create custom memes using this generator.
## What This Program Does:

### Summary
This program is designed to create a meme from a random
picture and pair it with a random quote. It also allows
users to enter their own pictures into the mix along with
their own creative captions. Once entered, the generator 
takes the users inputs and channels the random or set
output.

## To Get Started:

First, you will need to download 
some prerequisite libraries that may 
not be included in the IDE you're using.

### Prerequisites

In the root folder, there is a file called `Requirements.txt`. 
In here, you'll find all the versions required to run this program.
Install these by using:

```
pip install -r Requirements.txt
```

### Running

In order to start running this program, the user can
use this command:

```
python app.py
```

## Explaining The Code:

### Ingestor
#### What does it do:
The `__init__.py` file holds the main code for what happens
in the ingestor folder. In this file, the extensions
for each quote file is checked to then send it to its
respective ingestor functions in their python files.
#### Dependencies:
pandas -> https://pandas.pydata.org/

python to text -> https://python-docx.readthedocs.io/en/latest/

pdf to text -> https://www.xpdfreader.com/pdftotext-man.html

### Meme Engine
#### What does it do:
The `Meme_Engine.py` file included in the MemeEngine folder
holds the formatting and making for the meme itself. 
In here, the dimensions are shaped, the image is drawn,
and text is added to the image to create the meme.
#### Dependencies:
pillow  -> https://pillow.readthedocs.io/en/stable/

### Quote Engine
#### What does it do:
This folder holds a simple `__init__.py` file that
creates body and author objects and puts them together.

### app.py
#### What does it do:
This file holds the `setup()` function and all meme
functions to create your meme. It also, once finishing 
the meme creation, posts with a URL.

### meme.py
#### What does it do:
This file holds the `generate_meme()` function that
creates your meme and sends it to your `app.py` file.
This file also uses `ArgumentParser` to give help
messages for users.
