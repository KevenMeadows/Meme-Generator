import os
import random

from PIL import Image, ImageFont, ImageDraw


class MemeEngine:

    def __init__(self, output_dir):
        """Create self objects"""
        self.output_dir = output_dir
        self.count = 1
        """If no dir, create dir"""
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def format_and_make(self, img_path, text, author, width=500):
        """Open image"""
        image = Image.open(img_path)
        """Use os to connect image to output path"""
        outfile = os.path.join(self.output_dir, f"temp-{self.count}.jpg")
        self.count += 1
        """Get width and height of image for resize"""
        initialwidth = image.size
        initialheight = image.size
        """Resize"""
        height = int(initialheight * width / initialwidth)
        """Set new width and height"""
        image.thumbnail((width, height))
        """Create a position for text"""
        text_pos = random.choice(range(40, height - 40))
        """Outline and fill"""
        stroke = (255, 255, 255)
        fill = (0, 0, 0)
        """Draw image"""
        drawing = ImageDraw.Draw(image)
        """Format drawn image"""
        drawing.text((40, text_pos), text, fill, stroke_width=1, stroke_fill=stroke)
        drawing.text((55, text_pos + 20), f"- {author}", fill, stroke_width=1, stroke_fill=stroke)
        """Save image"""
        image.save(outfile, "JPEG")

        return outfile
