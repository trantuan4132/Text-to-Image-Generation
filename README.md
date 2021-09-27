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

Default fonts used in this repository is mainly used to generate Vietnamese name stamp, you can also try different fonts by placing truetype font files (.ttf) you wanted to use in a folder.

Then, you can start generating images using `main.py`:
```bash
$ python3 main.py -n <number-of-output-images> -l <number-of-lines-of-text> -t <text-file>
```

By default, images generated will have transparent background, red as text color and `font`, `font_title` folder as default font for name, job title respectively. You can change these setting by typing `$ python3 main.py --help` for more options on how to customize your images.

## Result

- Name stamp image generated:

![image](sample-output-1.png)

- Name stamp with job title image generated:

![image](sample-output-2.png)