from colormath.color_objects import sRGBColor, LabColor
from colormath.color_diff import delta_e_cie2000
from colormath.color_conversions import convert_color
from PIL import Image


def calculate_cie2000(filename1, filename2, pbar):
    res = 0

    img1 = Image.open(filename1)
    h, w = img1.size
    img1 = img1.load()
    img2 = Image.open(filename2).resize((h, w)).load()
    
    for x in range(h):
        for y in range(w):
            lab1 = convert_color(sRGBColor(*img1[x, y], is_upscaled=True), LabColor)
            lab2 = convert_color(sRGBColor(*img2[x, y], is_upscaled=True), LabColor)
            res += delta_e_cie2000(
                lab1,
                lab2
            )
            pbar.update()
    
    res /= h*w
    return res
