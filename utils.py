from PIL import Image, ImageDraw, ImageFont


def text_preprocessing(text):
    """
    Preprocess text for converting from Unicode to Vietnamese font.
    Arguments:
        text (str) -- Vietnamese text to be processed
    Returns:
        processed_text (str) -- Preprocessed Vietnamese text
    """
    converter = {           'à': 'aø', 'á': 'aù', 'ả': 'aû', 'ã': 'aõ', 'ạ': 'aï',
                            'è': 'eø', 'é': 'eù', 'ẻ': 'eû', 'ẽ': 'eõ', 'ẹ': 'eï',
                                                  'ỉ': 'æ',  'ĩ': 'ó',  'ị': 'ò',
                            'ò': 'oø', 'ó': 'où', 'ỏ': 'oû', 'õ': 'oõ', 'ọ': 'oï',
                            'ù': 'uø', 'ú': 'uù', 'ủ': 'uû', 'ũ': 'uõ', 'ụ': 'uï',
                 'ă': 'aê', 'ằ': 'aè', 'ắ': 'aé', 'ẳ': 'aú', 'ẵ': 'aü', 'ặ': 'aë',
                 'â': 'aâ', 'ầ': 'aà', 'ấ': 'aá', 'ẩ': 'aå', 'ẫ': 'aã', 'ậ': 'aä',
                 'ê': 'eâ', 'ề': 'eà', 'ế': 'eá', 'ể': 'eå', 'ễ': 'eã', 'ệ': 'eä',
                 'ô': 'oâ', 'ồ': 'oà', 'ố': 'oá', 'ổ': 'oå', 'ỗ': 'oã', 'ộ': 'oä',
                 'ơ': 'ô',  'ờ': 'ôø', 'ớ': 'ôù', 'ở': 'ôû', 'ỡ': 'ôõ', 'ợ': 'ôï',
                 'ư': 'ö',  'ừ': 'öø', 'ứ': 'öù', 'ử': 'öû', 'ữ': 'öõ', 'ự': 'öï',
                 'ỵ': 'î',  'đ': 'ñ'}

    processed_text = ''
    for char in text:
        if char.isupper():
            char = char.lower()
            char = converter.get(char, char)
            char = char.upper()
        else:
            char = converter.get(char, char)
        processed_text += char
    return processed_text


def gen_image_from_text(text, font_size, fontdir, text_color='#ff0000', transparent_bg=True):
    """
    Generate image with given text as content.
    Arguments:
        text (str) -- Text used in the content of image
        font_size (int) -- Size of text font
        font (str) -- Path to truetype font file (.ttf)
        color_code (str) -- Color of image in hex code format (Ex: #ffffff)
    Returns:
        image (PIL.Image) -- Image with transparent background and text as content 
    """
    # Get text font
    font = ImageFont.truetype(fontdir, size=font_size)

    # Processing text for VNI font only
    if font.getname()[0].startswith("VNI"):
        text = text_preprocessing(text)

    # Get the offset of text (the gap between starting coordination and first masking coordination)
    x_offset, y_offset = font.getoffset(text)

    # Get text size with given font
    width = font.getsize(text)[0]
    height = font.getsize(text)[1] - y_offset

    # Draw image with the same size as text
    alpha = 0 if transparent_bg else 255
    image = Image.new('RGBA', (width, height), color=(255, 255, 255, alpha))
    canvas = ImageDraw.Draw(image)

    # Add text to image
    canvas.text((-x_offset, -y_offset), text, font=font, fill=text_color)
    return image


if __name__ == "__main__":
    fontdirs = ['./font/VNI-TRIDICOnew.ttf',
                './font/VNI-Allegie.TTF',
                './font/VNI-Ariston.TTF', 
                './title_font/VNI-Helve.TTF',
                './title_font/VNI-Aptima.TTF',
                './title_font/Calibrib.TTF']

    gen_image_from_text(text='Nguyễn Văn A', 
                        font_size=80, 
                        fontdir=fontdirs[0], 
                        text_color='#2e5ab4', 
                        transparent_bg=False).show()