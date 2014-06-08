from PIL import Image
from PIL import ImageColor
from os import path

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CONTROL = (245, 246, 247)

def change_extension_to_bmp(org):
    root, ext = path.splitext(org)
    return root + '.bmp'

def save_as_bmp(path, png):
    bmp_path = change_extension_to_bmp(path)
    png.save(bmp_path, 'bmp', quality=80)
    png.show()

def convert_png_to_bmp(org):
    png = Image.open(org)
    png.load() # required for png.split()

    background = Image.new("RGB", png.size, CONTROL)
    background.paste(png, mask=png.split()[3]) # 3 is the alpha channel
    save_as_bmp(org, background)

png_path = 'sample.png'
convert_png_to_bmp(png_path)
