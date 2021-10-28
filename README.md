# text-to-image-generation

## Overview

This repository contains implementation of name stamp generation with text as foreground. 

Name stamp generated can have both job title and name (2 lines) or just name (1 line), transparent (no background) or non-transparent (white background).

This repository mainly focus on generate image with Vietnamese text but you can also generate image with English text as well.

You can also use some part of code in this repository to generate image for text detection.

## Installation

Clone this repository and install the dependencies:

```bash
$ git clone https://github.com/trantuan4132/Text-to-Image-Generation
$ cd Text-to-Image-Generation
$ pip install -r requirements.txt
```

## Usage

For generating name stamp only, your input file should contain text and each line will have the format of `{name}`, e.g.:

```
Nguyễn Văn An
Ngô Văn Quang
Lại Hồng Đăng
...
```

For generating name stamp with job title, your input file should contain text and each line will have the format of `{job title} | {name}`, e.g.:

```
Tổng giám đốc | Lê Đức Quang
Phó giám đốc | Ngô Văn Phúc
Trưởng nhóm | Hoàng Văn Lâm
...
```

If you only have file containing job titles only and you want concatenate each job title with all of the name listed in your other file, you can use the following command:
```bash
$ python3 concat_title_name.py

usage: concat_title_name.py [-h] [-n NAMEDIR] [-t TITLEDIR] [-o OUTDIR] [-lr MAX_LENGTH_RATIO]

Generate name stamp images from text

optional arguments:
  -h, --help            show this help message and exit
  -n NAMEDIR, --namedir NAMEDIR
                        Directory to file containing name
  -t TITLEDIR, --titledir TITLEDIR
                        Directory to file containing job title
  -o OUTDIR, --outdir OUTDIR
                        Path to file for saving output
  -lr MAX_LENGTH_RATIO, --max_length_ratio MAX_LENGTH_RATIO
                        The maximum length ratio of job title over name, only concat pair with smaller ratio than that
```

Default fonts used in this repository is mainly used to generate Vietnamese name stamp, you can also try different fonts by placing truetype font files (.ttf) you wanted to use in a folder.

Then, you can start generating images using `main.py`:
```
usage: main.py [-h] -n N_IMAGES -l N_LINES -t TEXTDIR [-o OUTDIR] [--name_font_size NAME_FONT_SIZE [NAME_FONT_SIZE ...]]
               [--title_font_size TITLE_FONT_SIZE [TITLE_FONT_SIZE ...]] [--name_fontdir NAME_FONTDIR] [--title_fontdir TITLE_FONTDIR]
               [--text_color TEXT_COLOR] [--transparent_bg] [--line_spacing LINE_SPACING [LINE_SPACING ...]] [--title_first_prob TITLE_FIRST_PROB]
               [--name_uppercase_prob NAME_UPPERCASE_PROB] [--title_uppercase_prob TITLE_UPPERCASE_PROB]
               [--title_name_max_width_ratio TITLE_NAME_MAX_WIDTH_RATIO] [--title_name_max_height_ratio TITLE_NAME_MAX_HEIGHT_RATIO]

Generate name stamp images from text

optional arguments:
  -h, --help            show this help message and exit
  -n N_IMAGES, --n_images N_IMAGES
                        Number of images to be generated
  -l N_LINES, --n_lines N_LINES
                        Number of lines of text to generate in a image (1 line for name stamp, 2 lines for name stamp with job title)
  -t TEXTDIR, --textdir TEXTDIR
                        Path to file containing text
  -o OUTDIR, --outdir OUTDIR
                        Path to folder for saving output images
  --name_font_size NAME_FONT_SIZE [NAME_FONT_SIZE ...]
                        Size of text font for name, enter 1 argument for fixed size (Ex: 40), enter 2 arguments for lower and upper bound of random size (Ex:   
                        20 40)
  --title_font_size TITLE_FONT_SIZE [TITLE_FONT_SIZE ...]
                        Size of text font for job title, enter 1 argument for fixed size (Ex: 20), enter 2 arguments for lower and upper bound of random size   
                        (Ex: 20 40)
  --name_fontdir NAME_FONTDIR
                        Path to .ttf file or folder containing fonts for name
  --title_fontdir TITLE_FONTDIR
                        Path to .ttf file or folder containing fonts for job title
  --text_color TEXT_COLOR
                        Color of text in hex code
  --transparent_bg      Generating transparent background if specified, generate white background otherwise
  --line_spacing LINE_SPACING [LINE_SPACING ...]
                        Spacing between lines of text for job title and name, enter 1 argument for fixed spacing (Ex: 15), enter 2 arguments for lower and      
                        upper bound of random spacing (Ex: 10 25)
  --title_first_prob TITLE_FIRST_PROB
                        Probability for job title to appear in 1st line (0.0 -> 1.0)
  --name_uppercase_prob NAME_UPPERCASE_PROB
                        Probability of text being converted to uppercase for name (0.0 -> 1.0)
  --title_uppercase_prob TITLE_UPPERCASE_PROB
                        Probability of text being converted to uppercase for job title (0.0 -> 1.0)
  --title_name_max_width_ratio TITLE_NAME_MAX_WIDTH_RATIO
                        Maximum width ratio of text for job title over text for name
  --title_name_max_height_ratio TITLE_NAME_MAX_HEIGHT_RATIO
                        Maximum height ratio of text for job title over text for name
```

**Note:** the command will output image with white background by default. If you want transparent background instead of white background, you can pass `--transparent_bg` as an argument to the command line

## Result

- Name stamp image generated:

![image](sample-output-1.png)

- Name stamp with job title image generated:

![image](sample-output-2.png)