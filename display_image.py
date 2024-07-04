import sys
import os
from waveshare_epd import epd7in5_V2
from PIL import Image

def main():
    try:
        epd = epd7in5_V2.EPD()
        epd.init()
        epd.Clear()

        image = Image.open('page.bmp')
        epd.display(epd.getbuffer(image))
        epd.sleep()

    except IOError as e:
        print(e)

    except KeyboardInterrupt:
        epd7in5_V2.epdconfig.module_exit()
        exit()

if __name__ == '__main__':
    main()
