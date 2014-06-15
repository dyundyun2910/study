# encoding: utf-8

from PIL import Image
from os import path

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CONTROL = (245, 246, 247)
PINK = (255, 0, 220)


def transparent_to_color(image, color=PINK):
    """
    alpha=255の部分をcolorで上書きし、alpha=0にする。

    Keyword Arguments:
    image -- PIL RGBA Image object
    color -- Tuple r, g, b (default 255, 255, 255)
    """ 
    im = image.copy()
    im.convert("RGBA")
    pixel_data = im.load()

    if im.mode == "RGBA":
        for y in range(im.size[1]): # each rows
            for x in range(im.size[0]): # each columns
                if pixel_data[x, y][3] == 0:
                    pixel_data[x, y] = PINK + (255,)
    return im

# α=0の部分を透過色にする
def transparent_to_color2(image, color=PINK):
    im = image.copy()
    im.load()
    mask = im.split()[3]
    pmask = mask.load()
    for y in range(mask.size[1]):
        for x in range(mask.size[0]):
            if pmask[x, y] == 0:
                pmask[x, y] = 255
            else:
                pmask[x, y] = 0

    foreground = Image.new("RGBA", image.size, color)
    im.paste(foreground, mask=mask)
    return im


# RGBA画像を指定した色とブレンドする
def alpha_to_color(image, color=WHITE):
    image.load()
    background = Image.new("RGB", image.size, color)
    background.paste(image, mask=image.split()[3]) # 3 is the alpha channel
    return background

# 拡張子をBMPに変更する
def change_extension_to_bmp(org):
    root, ext = path.splitext(org)
    return root + ".bmp"

### script
import time
t_start = time.clock()

png_path = 'sample.png'
png = Image.open(png_path, 'r')
png_trans = transparent_to_color(png)
blended = alpha_to_color(png_trans, CONTROL)
blended.save(change_extension_to_bmp(png_path), 'BMP', quality=80)

t_end = time.clock()
t = t_end - t_start
t = int(t)
t = str(t)
print("処理時間:" + t)

# blended.show()
