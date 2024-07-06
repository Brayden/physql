import sys
import os
from waveshare_epd import epd7in5_V2
from PIL import Image

def main():
    try:
        # epd = epd7in5_V2.EPD()
        # epd.init()
        # epd.Clear()

        # # Open the PNG file and convert it to BMP
        # png_image = Image.open('page.png')
        # bmp_image = png_image.convert('1')
        # bmp_image.save('page.bmp')

        # # Display the BMP image on the e-paper screen
        # image = Image.open('page.bmp')
        # epd.display(epd.getbuffer(image))
        # epd.sleep()

        epd = epd7in5_V2.EPD()
        epd.init()

        # Open the PNG file and convert it to BMP
        png_image = Image.open('page.png')
        bmp_image = png_image.convert('1')
        bmp_image.save('page.bmp')

        # Display the BMP image on the e-paper screen
        image = Image.open('page.bmp')
        epd.display(epd.getbuffer(image))

        # Use partial update instead of full clear
        epd.displayPartBaseImage(epd.getbuffer(image))
        epd.displayPartial(epd.getbuffer(image))

        epd.sleep()

    except IOError as e:
        print(e)

    except KeyboardInterrupt:
        epd7in5_V2.epdconfig.module_exit()
        exit()

if __name__ == '__main__':
    main()
