#!/usr/bin/env python3

import sys
import os
from waveshare_epd import epd7in5_V2
from PIL import Image, ImageDraw, ImageFont

def main():
    try:
        print("Initializing the e-paper display...")
        epd = epd7in5_V2.EPD()
        epd.init()
        epd.Clear()

        print("Creating an image object...")
        # Create an image object
        image = Image.new('1', (epd7in5_V2.EPD_WIDTH, epd7in5_V2.EPD_HEIGHT), 255)  # 1-bit color, white background
        draw = ImageDraw.Draw(image)

        print("Loading a built-in bitmap font...")
        # Use a larger built-in bitmap font
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)  # Adjust the size as needed

        print("Drawing text on the image...")
        # Draw the text "phySQL" on the image
        text = "phySQL"
        text_width, text_height = draw.textsize(text, font=font)
        x = (epd7in5_V2.EPD_WIDTH - text_width) // 2
        y = (epd7in5_V2.EPD_HEIGHT - text_height) // 2
        draw.text((x, y), text, font=font, fill=0)

        print("Displaying the image on the e-paper screen...")
        # Display the image on the e-paper screen
        epd.display(epd.getbuffer(image))

        print("Putting the e-paper display to sleep...")
        epd.sleep()

    except IOError as e:
        print(f"IOError: {e}")

    except KeyboardInterrupt:
        print("KeyboardInterrupt detected, exiting...")
        epd7in5_V2.epdconfig.module_exit()
        exit()

if __name__ == '__main__':
    main()
