#!/usr/bin/env python3

import sys
import os
from waveshare_epd import epd7in5_V2
from PIL import Image, ImageDraw, ImageFont

def main():
    try:
        epd = epd7in5_V2.EPD()
        epd.init()
        epd.Clear()

        # Create an image object
        image = Image.new('1', (epd7in5_V2.EPD_WIDTH, epd7in5_V2.EPD_HEIGHT), 255)  # 1-bit color, white background
        draw = ImageDraw.Draw(image)
        
        # Use a truetype font
        font = ImageFont.load_default()

        # Draw the text "phySQL" on the image
        draw.text((10, 10), "phySQL", font=font, fill=0)

        # Display the image on the e-paper screen
        epd.display(epd.getbuffer(image))

        epd.sleep()

    except IOError as e:
        print(e)

    except KeyboardInterrupt:
        epd7in5_V2.epdconfig.module_exit()
        exit()

if __name__ == '__main__':
    main()
