import os
import argparse
from datetime import datetime
import random
from PIL import Image
from utils import gen_image_from_text


def parse_args():
    parser = argparse.ArgumentParser(description="Generate name stamp images from text")
    parser.add_argument('-n', '--n_images', type=int, required=True, 
                        help="Number of images to be generated") 
    parser.add_argument('-l', '--n_lines', type=int, required=True, 
                        help="Number of lines of text to generate in a image (1 line for name stamp, 2 lines for name stamp with job title)")
    parser.add_argument('-t', '--textdir', type=str, required=True, 
                        help="Path to file containing text")
    parser.add_argument('-o', '--outdir', type=str, default="./output", required=False, 
                        help="Path to folder for saving output images")
    parser.add_argument('--name_font_size', type=int, nargs='+', default=[40], required=False, 
                        help="Size of text font for name, enter 1 argument for fixed size (Ex: 40), \
                              enter 2 arguments for lower and upper bound of random size (Ex: 20 40)")
    parser.add_argument('--title_font_size', type=int, nargs='+', default=[20, 30], required=False, 
                        help="Size of text font for job title, enter 1 argument for fixed size (Ex: 20), \
                              enter 2 arguments for lower and upper bound of random size (Ex: 20 40)")
    parser.add_argument('--name_fontdir', type=str, default="./font", required=False, 
                        help="Path to .ttf file or folder containing fonts for name")
    parser.add_argument('--title_fontdir', type=str, default="./title_font", required=False, 
                        help="Path to .ttf file or folder containing fonts for job title")
    parser.add_argument('--text_color', type=str, default="#ff0000", required=False, 
                        help="Color of text in hex code")
    parser.add_argument('--transparent_bg', action="store_true", default=False, required=False, 
                        help="Generating transparent background if specified, generate white background otherwise")
    parser.add_argument('--line_spacing', type=int, nargs='+', default=[10, 25], required=False, 
                        help="Spacing between lines of text for job title and name, enter 1 argument for fixed spacing (Ex: 15), \
                              enter 2 arguments for lower and upper bound of random spacing (Ex: 10 25)")
    parser.add_argument('--title_first_prob', type=float, default=1.0, required=False, 
                        help="Probability for job title to appear in 1st line (0.0 -> 1.0)")
    parser.add_argument('--name_uppercase_prob', type=float, default=0.0, required=False, 
                        help="Probability of text being converted to uppercase for name (0.0 -> 1.0)")
    parser.add_argument('--title_uppercase_prob', type=float, default=1.0, required=False, 
                        help="Probability of text being converted to uppercase for job title (0.0 -> 1.0)")
    parser.add_argument('--title_name_max_width_ratio', type=float, default=None, required=False, 
                        help="Maximum width ratio of text for job title over text for name")
    parser.add_argument('--title_name_max_height_ratio', type=float, default=None, required=False, 
                        help="Maximum height ratio of text for job title over text for name")
    args = parser.parse_args()
    return args


class NameStampGenerator(object):
    def __init__(
        self, 
        textdir, 
        name_font_size=[80], 
        title_font_size=[40], 
        name_fontdir="./font", 
        title_fontdir="./title_font", 
        text_color='#ff0000', 
        transparent_bg=True,
        line_spacing=[15],
        title_first_prob=1.0,
        name_uppercase_prob=0.0,
        title_uppercase_prob=1.0,
        max_width_ratio=None,
        max_height_ratio=None,
        outdir="./output"
    ):
        self.texts = self.load_text(textdir)
        self.name_font_size = name_font_size
        self.title_font_size = title_font_size
        self.name_font_subdirs = self.load_fontdirs(name_fontdir)
        self.title_font_subdirs = self.load_fontdirs(title_fontdir)
        self.text_color = text_color
        self.transparent_bg = transparent_bg
        self.line_spacing = line_spacing
        self.title_first_prob = title_first_prob
        self.name_uppercase_prob = name_uppercase_prob
        self.title_uppercase_prob = title_uppercase_prob
        self.max_width_ratio = max_width_ratio
        self.max_height_ratio = max_height_ratio
        self.outdir = outdir
        os.makedirs(self.outdir, exist_ok=True)

    def load_text(self, textdir):
        """
        Load list of text from file
        """
        texts = []
        with open(textdir, encoding='utf-8') as file:
            for line in file:
                if len(line.strip()) > 0:
                    line = line.strip().split('|')
                    line = list(filter(bool, line))
                    texts.append(line)
        return texts

    def load_fontdirs(self, fontdir):
        """
        Load list of truetype font file paths from folder
        """
        font_subdirs = []
        if fontdir.lower().endswith('.ttf'):
            font_subdirs.append(fontdir)
        else:
            for file in os.listdir(fontdir):
                font_subdirs.append(os.path.join(fontdir, file))
        return font_subdirs
        
    def process_text(self, text, upper_prob):
        if random.random() < upper_prob:
            return text.strip().upper()
        else:
            return text.strip()

    def get_size(self, sizes):
        """
        Return fixed size when there is only a size given, 
        otherwise return random size in the range of first two sizes.
        """
        if len(sizes) == 1:
            return sizes[0]
        else: 
            return random.randint(*sizes[:2])

    def gen_name_stamp_only(self, n_images):
        """
        Generate image with 1-line text as name stamp
        """
        for i in range(n_images):
            # Select text from list at random and process text 
            text = random.choice(self.texts)[0]
            text = self.process_text(text, self.name_uppercase_prob)

            # Select font directory from list at random
            fontdir = random.choice(self.name_font_subdirs)

            # Get font size
            font_size = self.get_size(self.name_font_size)

            # Generate image
            image = gen_image_from_text(text, font_size, fontdir=fontdir, 
                                        text_color=self.text_color, transparent_bg=self.transparent_bg)

            # Save generated image
            filename = datetime.now().strftime(f"%Y_%m_%d_%H_%M_%S_%f_{i}.png")
            image.save(os.path.join(self.outdir, filename))

    def gen_name_stamp_with_job_title(self, n_images):
        """Generate image with 2-line text (1st line for job title, 2nd line for name) """
        for i in range(n_images):
            # Select text from list at random and process text 
            title, name = random.choice(self.texts)
            title = self.process_text(title, self.title_uppercase_prob)
            name = self.process_text(name, self.name_uppercase_prob)

            # Select font directory from list at random
            name_fontdir = random.choice(self.name_font_subdirs)
            if len(self.title_font_subdirs) > 0:
                title_fontdir = random.choice(self.title_font_subdirs)
            else:
                title_fontdir = name_fontdir

            # Get font size and line spacing
            name_font_size = self.get_size(self.name_font_size)
            title_font_size = self.get_size(self.title_font_size)
            line_spacing = self.get_size(self.line_spacing)

            # Generate image for job title and name
            title_image = gen_image_from_text(title, title_font_size, fontdir=title_fontdir,
                                              text_color=self.text_color, transparent_bg=self.transparent_bg)
            name_image = gen_image_from_text(name, name_font_size, fontdir=name_fontdir, 
                                             text_color=self.text_color, transparent_bg=self.transparent_bg)

            # Get the size of generated images
            w_name, h_name = name_image.size[:2]
            w_title, h_title = title_image.size[:2]

            # Resize job title image using max width and height ratio if given
            max_w_title = int(w_name * self.max_width_ratio) if self.max_width_ratio else w_title
            max_h_title = int(h_name * self.max_height_ratio) if self.max_height_ratio else h_title
            w_title = min(w_title, max_w_title)
            h_title = min(h_title, max_h_title)
            title_image = title_image.resize([w_title, h_title], Image.ANTIALIAS)

            # Create a new image
            width = max(w_title, w_name)
            height = h_title + line_spacing + h_name
            alpha = 0 if self.transparent_bg else 255
            image = Image.new('RGBA', (width, height), color=(255, 255, 255, alpha))

            # Paste all generated images into the new image
            if random.random() < self.title_first_prob:
                image.paste(title_image, ((width - w_title) // 2, 0), title_image)
                image.paste(name_image, ((width - w_name) // 2, h_title + line_spacing), name_image)
            else:
                image.paste(name_image, ((width - w_name) // 2, 0), name_image)
                image.paste(title_image, ((width - w_title) // 2, h_name + line_spacing), title_image)

            # Save generated image
            filename = datetime.now().strftime(f"%Y_%m_%d_%H_%M_%S_%f_{i}.png")
            image.save(os.path.join(self.outdir, filename))


def main():
    args = parse_args()
    # print(args)
        
    # Generate image with text
    generator = NameStampGenerator(textdir=args.textdir, 
                                   name_font_size=args.name_font_size, 
                                   title_font_size=args.title_font_size, 
                                   name_fontdir=args.name_fontdir, 
                                   title_fontdir=args.title_fontdir,
                                   text_color=args.text_color,
                                   transparent_bg=args.transparent_bg, 
                                   line_spacing=args.line_spacing,
                                   title_first_prob=args.title_first_prob,
                                   name_uppercase_prob=args.name_uppercase_prob,
                                   title_uppercase_prob=args.title_uppercase_prob,
                                   max_width_ratio=args.title_name_max_width_ratio,
                                   max_height_ratio=args.title_name_max_height_ratio,
                                   outdir=args.outdir)

    if int(args.n_lines) == 1:
        generator.gen_name_stamp_only(args.n_images)
    elif int(args.n_lines) == 2:
        generator.gen_name_stamp_with_job_title(args.n_images)

    print("Finished")


if __name__ == "__main__":
    main()