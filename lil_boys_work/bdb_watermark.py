#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: Hari

Source:
    https://medium.com/better-programming/add-copyright-or-watermark-to-photos-using-python-a3773c71d431

    /Users/rajacsp/datasets

    https://www.fontspace.com/category/ttf

    https://www.1001freefonts.com/decorative-fonts.php

    https://drive.google.com/drive/folders/1eHDFJIGGGCtNZXpIthBf6hp97CqhcZVM

    /Users/rajacsp/datasets/fonts/Open_Sans/

    https://fonts.google.com/

    https://stackoverflow.com/questions/43708681/pil-png-image-as-watermark-for-a-jpg-image

    https://stackoverflow.com/questions/54366843/how-to-resize-png-image-in-opencv-python
'''

# Import necessary modules 
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

FOLDER_LOCAITON = '/Users/rajacsp/d/tact/The Big Data Boss/BDB-Memes/Lil-Boys/'

FILENAME        = 'BDB_Meme_1002.jpg'
OUTPUT_FILENAME = 'test_watermark.jpg'

FONT_LOCAITON = '/Users/rajacsp/datasets/fonts/Open_Sans/OpenSans-Light.ttf'

WATERMARK_LOCATION = '/Users/rajacsp/d/tact/The Big Data Boss/logo/Big_Data_Boss_Final.png'

RESIZE_FACTOR = 0.02

def apply_watermark_image(input_path, output_path):

    photo = Image.open(input_path)
    watermark = Image.open(WATERMARK_LOCATION)

    ph_width, ph_height = photo.size
    wm_width, wm_height = watermark.size

    wm_witdh_new = int(wm_width * RESIZE_FACTOR)
    wm_height_new = int(wm_height * RESIZE_FACTOR)

    watermark = watermark.resize((wm_witdh_new, wm_height_new))
    
    photo.paste(watermark, ((ph_width - wm_height_new - 150), (ph_height - wm_height_new - 70)), watermark)

    photo.save(output_path)

def apply_watermark_text(input_path, output_path, watermark_text):

    photo = Image.open(input_path)

    output_image_path = output_path
 
    #Store image width and height
    w, h = photo.size
    # print(w, h)

    # make the image editable
    drawing = ImageDraw.Draw(photo)
    font = ImageFont.truetype(FONT_LOCAITON, 50)

    #get text width and height
    text_w, text_h = drawing.textsize(watermark_text, font)

    pos = w - text_w, (h - text_h) - 50
    
    c_text = Image.new('RGB', (text_w, (text_h)), color = '#000000')
    drawing = ImageDraw.Draw(c_text)
    
    drawing.text((0, 0), watermark_text, fill="#ffffff", font=font)
    c_text.putalpha(100)
   
    photo.paste(c_text, pos, c_text)
    photo.save(output_image_path)

def startpy():

    input_path = FOLDER_LOCAITON + FILENAME
    output_path = FOLDER_LOCAITON + OUTPUT_FILENAME
    
    # apply_watermark_text(input_path, output_path, '@bigdataboss/')

    apply_watermark_image(input_path, output_path)


if __name__ == '__main__':
    startpy()