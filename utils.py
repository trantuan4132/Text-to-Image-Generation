from PIL import Image, ImageDraw, ImageFont


def convert_character_encoding(text, src="Unicode", dst="VNIWin"):
    """
    Converting each character of text from the current character encoding to another.

    Arguments
    ---------
        text : str 
            Vietnamese text to be processed

    Returns
    -------
        processed_text : str
            Preprocessed Vietnamese text
    """
    Unicode = [
        u'â',u'Â',u'ă',u'Ă',u'đ',u'Đ',u'ê',u'Ê',u'ô',u'Ô',u'ơ',u'Ơ',u'ư',u'Ư',u'á',u'Á',u'à',u'À',u'ả',u'Ả',u'ã',u'Ã',u'ạ',u'Ạ',
        u'ấ',u'Ấ',u'ầ',u'Ầ',u'ẩ',u'Ẩ',u'ẫ',u'Ẫ',u'ậ',u'Ậ',u'ắ',u'Ắ',u'ằ',u'Ằ',u'ẳ',u'Ẳ',u'ẵ',u'Ẵ',u'ặ',u'Ặ',
        u'é',u'É',u'è',u'È',u'ẻ',u'Ẻ',u'ẽ',u'Ẽ',u'ẹ',u'Ẹ',u'ế',u'Ế',u'ề',u'Ề',u'ể',u'Ể',u'ễ',u'Ễ',u'ệ',u'Ệ',u'í',u'Í',u'ì',u'Ì',u'ỉ',u'Ỉ',u'ĩ',u'Ĩ',u'ị',u'Ị',    
        u'ó',u'Ó',u'ò',u'Ò',u'ỏ',u'Ỏ',u'õ',u'Õ',u'ọ',u'Ọ',u'ố',u'Ố',u'ồ',u'Ồ',u'ổ',u'Ổ',u'ỗ',u'Ỗ',u'ộ',u'Ộ',u'ớ',u'Ớ',u'ờ',u'Ờ',u'ở',u'Ở',u'ỡ',u'Ỡ',u'ợ',u'Ợ',    
        u'ú',u'Ú',u'ù',u'Ù',u'ủ',u'Ủ',u'ũ',u'Ũ',u'ụ',u'Ụ',u'ứ',u'Ứ',u'ừ',u'Ừ',u'ử',u'Ử',u'ữ',u'Ữ',u'ự',u'Ự',u'ỳ',u'Ỳ',u'ỷ',u'Ỷ',u'ỹ',u'Ỹ',u'ỵ',u'Ỵ',u'ý',u'Ý'    
    ]

    TCVN3 = [
        u'©',u'¢',u'¨',u'¡',u'®',u'§',u'ª',u'£',u'«',u'¤',u'¬',u'¥',u'­',u'¦',u'¸',u'¸',u'µ',u'µ',u'¶',u'¶',u'·',u'·',u'¹',u'¹',
        u'Ê',u'Ê',u'Ç',u'Ç',u'È',u'È',u'É',u'É',u'Ë',u'Ë',u'¾',u'¾',u'»',u'»',u'¼',u'¼',u'½',u'½',u'Æ',u'Æ',
        u'Ð',u'Ð',u'Ì',u'Ì',u'Î',u'Î',u'Ï',u'Ï',u'Ñ',u'Ñ',u'Õ',u'Õ',u'Ò',u'Ò',u'Ó',u'Ó',u'Ô',u'Ô',u'Ö',u'Ö',u'Ý',u'Ý',u'×',u'×',u'Ø',u'Ø',u'Ü',u'Ü',u'Þ',u'Þ',    
        u'ã',u'ã',u'ß',u'ß',u'á',u'á',u'â',u'â',u'ä',u'ä',u'è',u'è',u'å',u'å',u'æ',u'æ',u'ç',u'ç',u'é',u'é',u'í',u'í',u'ê',u'ê',u'ë',u'ë',u'ì',u'ì',u'î',u'î',    
        u'ó',u'ó',u'ï',u'ï',u'ñ',u'ñ',u'ò',u'ò',u'ô',u'ô',u'ø',u'ø',u'õ',u'õ',u'ö',u'ö',u'÷',u'÷',u'ù',u'ù',u'ú',u'ú',u'û',u'û',u'ü',u'ü',u'þ',u'þ',u'ý',u'ý'     
    ]

    VNIWin = [
        u'aâ',u'AÂ',u'aê',u'AÊ',u'ñ',u'Ñ',u'eâ',u'EÂ',u'oâ',u'OÂ',u'ô',u'Ô',u'ö',u'Ö',u'aù',u'AÙ',u'aø',u'AØ',u'aû',u'AÛ',u'aõ',u'AÕ',u'aï',u'AÏ',
        u'aá',u'AÁ',u'aà',u'AÀ',u'aå',u'AÅ',u'aã',u'AÃ',u'aä',u'AÄ',u'aé',u'AÉ',u'aè',u'AÈ',u'aú',u'AÚ',u'aü',u'AÜ',u'aë',u'AË',
        u'eù',u'EÙ',u'eø',u'EØ',u'eû',u'EÛ',u'eõ',u'EÕ',u'eï',u'EÏ',u'eá',u'EÁ',u'eà',u'EÀ',u'eå',u'EÅ',u'eã',u'EÃ',u'eä',u'EÄ',u'í',u'Í',u'ì',u'Ì',u'æ',u'Æ',u'ó',u'Ó',u'ò',u'Ò',    
        u'où',u'OÙ',u'oø',u'OØ',u'oû',u'OÛ',u'oõ',u'OÕ',u'oï',u'OÏ',u'oá',u'OÁ',u'oà',u'OÀ',u'oå',u'OÅ',u'oã',u'OÃ',u'oä',u'OÄ',u'ôù',u'ÔÙ',u'ôø',u'ÔØ',u'ôû',u'ÔÛ',u'ôõ',u'ÔÕ',u'ôï',u'ÔÏ',    
        u'uù',u'UÙ',u'uø',u'UØ',u'uû',u'UÛ',u'uõ',u'UÕ',u'uï',u'UÏ',u'öù',u'ÖÙ',u'öø',u'ÖØ',u'öû',u'ÖÛ',u'öõ',u'ÖÕ',u'öï',u'ÖÏ',u'yø',u'YØ',u'yû',u'YÛ',u'yõ',u'YÕ',u'î',u'Î',u'yù',u'YÙ'    
    ]

    processed_text = ''
    for char in text:
        try:
            char = eval(f"{dst}[{src}.index(char)]")
        except:
            pass
        processed_text += char
    return processed_text


def gen_image_from_text(text, font_size, fontdir, text_color='#ff0000', transparent_bg=True):
    """
    Generate image with given text as content.

    Arguments
    ---------
        text : str 
            Text used in the content of image
        font_size : int 
            Size of text font
        font : str 
            Path to truetype font file (.ttf)
        color_code : str 
            Color of image in hex code format (Ex: #ffffff)
        
    Returns
    -------
        image : PIL.Image
            Image with transparent background and text as content 
    """
    # Get text font
    font = ImageFont.truetype(fontdir, size=font_size)

    # Processing text for VNI font only
    if font.getname()[0].upper().startswith("VNI"):
        text = convert_character_encoding(text, dst="VNIWin")
    elif font.getname()[0].upper().startswith(".VN"):
        text = convert_character_encoding(text, dst="TCVN3")

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


def rescale_by_height(image, height_range):
    """
    Rescale image so that its height is in given range.
    If its height is smaller than minimum height, it will be rescaled to achieve that minimum height.
    If its height is larger than maximum height, it will be rescaled to achieve that maximum height.
    If its height is already in given range, no rescaling is needed.

    Arguments
    ---------
        image : PIL.Image
            Image to be rescaled
        height_range : list or tuple of ints
            Height range for image to be rescaled

    Returns
    -------
        new_image : PIL.Image 
            Rescaled image
    """
    # Get size of image
    w, h = image.size[:2]

    # Get minimum and maximum height for image to be rescaled
    if len(height_range) == 1:
        h_min = h_max = height_range[0]
    else:
        h_min, h_max = height_range[:2]

    # Rescale image
    if h < h_min:
        # Upscale image
        new_w, new_h = int(w * h_min/h), h_min
        new_image = image.resize((new_w, new_h), Image.BICUBIC)
    elif h > h_max:
        # Downscale image
        new_w, new_h = int(w * h_max/h), h_max
        new_image = image.resize((new_w, new_h), Image.ANTIALIAS)
    else:
        # Keep the original image
        new_image = image
    return new_image


if __name__ == "__main__":
    fontdirs = ['./font/VNI-TRIDICOnew.ttf',
                './font/VNI-Allegie.TTF',
                './font/VNI-Ariston.TTF',
                './font/VHTIME.TTF', 
                './title_font/VNI-Helve.TTF',
                './title_font/VNI-Aptima.TTF',
                './title_font/Calibrib.TTF']

    gen_image_from_text(text='Nguyễn Văn A', 
                        font_size=80, 
                        fontdir=fontdirs[0], 
                        text_color='#3353b1', 
                        transparent_bg=False).show()

    # img = Image.new('RGB', (500, 500), color=(255, 255, 255))
    # print(rescale_by_height(img, [200, 400]).size)