#!/usr/bin/env python3

import sys
import os
from waveshare_epd import epd7in5_V2
from PIL import Image

def main():
    try:
        epd = epd7in5_V2.EPD()
        epd.init()
        epd.Clear()

        # Draw the text "PHYSQL" on the e-paper screen
        image = Image.new('1', (epd7in5_V2.EPD_HEIGHT, epd7in5_V2.EPD_WIDTH), 255)
        epd.display_string_at(image, 10, 10, "phySQL", 16, 0)
        epd.display(epd.getbuffer(image))

        epd.sleep()

    except IOError as e:
        print(e)

    except KeyboardInterrupt:
        epd7in5_V2.epdconfig.module_exit()
        exit()

if __name__ == '__main__':
    main()
