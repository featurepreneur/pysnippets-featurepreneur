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
'''

# Import necessary modules 
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

FOLDER_LOCAITON = '/Users/rajacsp/datasets/'

FILENAME        = 'BDB_Meme_1014.jpg'
OUTPUT_FILENAME = 'BDB_Meme_1014_watermark.jpg'

def apply_watermark(input_path, output_path, watermark_text):

    photo = Image.open(input_path)

    output_image_path = output_path
 
    #Store image width and height
    w, h = photo.size
    # print(w, h)

    # make the image editable
    drawing = ImageDraw.Draw(photo)
    font = ImageFont.truetype("/Users/rajacsp/datasets/fonts/Drift.ttf", 68)

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
    
    apply_watermark(input_path, output_path, '@bigdataboss/')


if __name__ == '__main__':
    startpy()