import os
import argparse
from datetime import datetime
import random
from PIL import Image
from utils import gen_image_from_text


def parse_args():
    parser = argparse.ArgumentParser(description="Generate name stamp images from text")
    parser.add_argument('-n', '--n_images', type=int, help="Number of images to be generated", required=True) 
    parser.add_argument('-l', '--n_lines', type=int, help="Number of lines of text to generate in a image (1 line for name stamp, 2 lines for name stamp with job title)", required=True)
    parser.add_argument('-t', '--textdir', type=str, help="Path to file containing text", required=True)
    parser.add_argument('-ns', '--name_font_size', type=int, help="Size of text font for name", default=48, required=False)
    parser.add_argument('-ts', '--title_font_size', type=int, help="Size of text font for job title", default=28, required=False)
    parser.add_argument('-nf', '--name_fontdir', type=str, help="Path to folder containing font for name", default="./font", required=False)
    parser.add_argument('-tf', '--title_fontdir', type=str, help="Path to folder containing font for job title", default="./title_font", required=False)
    parser.add_argument('-tc', '--text_color', type=str, help="Color of text in hex code", default="#ff0000", required=False)
    parser.add_argument('-tb', '--transparent_bg', type=str, help="Set to True for generating transparent background, set to False otherwise", default=True, required=False)
    parser.add_argument('-o', '--outdir', type=str, help="Path to folder for saving output images", default="./output", required=False)
    args = parser.parse_args()
    return args


class NameStampGenerator(object):
    def __init__(
        self, 
        texts, 
        name_font_size=80, 
        title_font_size=40, 
        name_fontdirs=[], 
        title_fontdirs=[], 
        text_color='#ff0000', 
        transparent_bg=True,
        outdir="./output"
    ):
        self.texts = texts
        self.name_font_size = name_font_size
        self.title_font_size = title_font_size
        self.name_fontdirs = name_fontdirs
        self.title_fontdirs = title_fontdirs
        self.text_color = text_color
        self.transparent_bg = transparent_bg
        self.outdir = outdir


    def gen_name_stamp_only(self, n_images):
        """Generate image with 1-line text as name stamp"""
        for i in range(n_images):
            # Select text and font directory from list at random
            text = random.choice(self.texts)
            fontdir = random.choice(self.name_fontdirs)

            # Generate image
            image = gen_image_from_text(text, self.name_font_size, fontdir=fontdir, 
                                        text_color=self.text_color, transparent_bg=self.transparent_bg)

            # Save generated image
            filename = datetime.now().strftime(f"%Y_%m_%d_%H_%M_%S_%f_{i}.png")
            image.save(os.path.join(self.outdir, filename))


    def gen_name_stamp_with_job_title(self, n_images):
        """Generate image with 2-line text (1st line for job title, 2nd line for name) """
        for i in range(n_images):
            # Select text and font directory from list at random
            text = random.choice(self.texts)
            title, name = text.split('|')
            title = title.strip().upper()
            name = name.strip()
            name_fontdir = random.choice(self.name_fontdirs)
            if len(self.title_fontdirs) > 0:
                title_fontdir = random.choice(self.title_fontdirs)
            else:
                title_fontdir = name_fontdir

            # Generate image for job title and name
            title_image = gen_image_from_text(title, self.title_font_size, fontdir=title_fontdir,
                                              text_color=self.text_color, transparent_bg=self.transparent_bg)
            name_image = gen_image_from_text(name, self.name_font_size, fontdir=name_fontdir, 
                                             text_color=self.text_color, transparent_bg=self.transparent_bg)

            # Get the size of each generated image
            w_title, h_title = title_image.size[:2]
            w_name, h_name = name_image.size[:2]

            # Create a new image
            line_spacing = random.randint(10, 30)
            width = max(w_title, w_name)
            height = h_title + line_spacing + h_name
            alpha = 0 if self.transparent_bg else 255
            image = Image.new('RGBA', (width, height), color=(255, 255, 255, alpha))

            # Paste all generated images into the new image
            image.paste(title_image, ((width - w_title) // 2, 0), title_image)
            image.paste(name_image, ((width - w_name) // 2, h_title + line_spacing), name_image)

            # Save generated image
            filename = datetime.now().strftime(f"%Y_%m_%d_%H_%M_%S_%f_{i}.png")
            image.save(os.path.join(self.outdir, filename))


def main():
    args = parse_args()

    # Check for output directory
    if not os.path.exists(args.outdir):
        os.makedirs(args.outdir)

    # Load list of text from file
    with open(args.textdir, encoding='utf-8') as file:
        texts = file.read().split('\n')

    # Load name font from directory
    name_fontdirs = []
    for file in os.listdir(args.name_fontdir):
        name_fontdirs.append(os.path.join(args.name_fontdir, file))

    # Load job title font from directory
    title_fontdirs = []
    if args.title_fontdir is not None:
        for file in os.listdir(args.title_fontdir):
            title_fontdirs.append(os.path.join(args.title_fontdir, file))

    # Generate image with text
    generator = NameStampGenerator(texts, 
                                   name_font_size=args.name_font_size, 
                                   title_font_size=args.title_font_size, 
                                   name_fontdirs=name_fontdirs, 
                                   title_fontdirs=title_fontdirs,
                                   text_color=args.text_color,
                                   transparent_bg=args.transparent_bg, 
                                   outdir=args.outdir)
    if int(args.n_lines) == 1:
        generator.gen_name_stamp_only(args.n_images)
    elif int(args.n_lines) == 2:
        generator.gen_name_stamp_with_job_title(args.n_images)

    print("Finished")


if __name__ == "__main__":
    main()