import math
from decimal import Decimal

from numpy import vectorize, uint8
from scipy.misc import imread, toimage, imsave


class Bitmap8BitGrey:
    def __init__(self, path):
        self.path = path
        self.pixels = imread(self.path, flatten=True, mode='L')
        self.modify_pixels = self.pixels.copy()
        self.preview_pixels = self.pixels.copy()

        self.size = self.pixels.shape

    def to_image(self):
        return toimage(self.preview_pixels, mode='L')

    def save(self):
        imsave(self.path, self.modify_pixels)
        self.pixels = self.modify_pixels.copy()

    def save_as(self, path, extension):
        extensions = {"BMP Image (.bmp)": "bmp",
                      "PNG Image (.png)": "png",
                      "JPG Image (.jpg)": "jpg"}
        save_as_path = "{name}.{extension}".format(name=path, extension=extensions[extension])
        imsave(save_as_path, self.modify_pixels)

    def histogram_of_brightness(self, point_left_top, point_right_bottom):
        return self.preview_pixels[
               point_left_top[1]:point_right_bottom[1],
               point_left_top[0]:point_right_bottom[0]].ravel()

    def change_brightness(self, value, point_left_top, point_right_bottom):
        def set_pix_brightness(pix):
            new_pix = int(pix) + value
            if new_pix > 255:
                return uint8(255)
            if new_pix < 0:
                return uint8(0)
            return uint8(new_pix)

        table_brightness = [set_pix_brightness(pix) for pix in range(256)]
        vfunc_brightness = vectorize(lambda pix: table_brightness[int(pix)])

        self.preview_pixels[
        point_left_top[1]:point_right_bottom[1],
        point_left_top[0]:point_right_bottom[0]
        ] = vfunc_brightness(self.modify_pixels[
                             point_left_top[1]:point_right_bottom[1],
                             point_left_top[0]:point_right_bottom[0]].copy())

    def change_contrast(self, value, point_left_top, point_right_bottom):
        factor = Decimal((259.0 * (value + 255)) / (255.0 * (259 - value)))

        def set_pix_contrast(pix):
            new_pix = Decimal(128 + factor * (int(pix) - 128))
            if new_pix > 255:
                return uint8(255)
            if new_pix < 0:
                return uint8(0)
            return uint8(new_pix)

        table_contrast = [set_pix_contrast(pix) for pix in range(256)]
        vfunc_contrast = vectorize(lambda pix: table_contrast[int(pix)])

        self.preview_pixels[
        point_left_top[1]:point_right_bottom[1],
        point_left_top[0]:point_right_bottom[0]
        ] = vfunc_contrast(self.modify_pixels[
                           point_left_top[1]:point_right_bottom[1],
                           point_left_top[0]:point_right_bottom[0]].copy())

    def change_gamma(self, value, point_left_top, point_right_bottom):
        gamma = value/2 + 1 if value >= 0 else (1.0 / abs(value))

        def set_pix_gamma(pix):
            new_pix = Decimal(255.0 * (math.pow(pix / 255, gamma)))
            if new_pix > 255:
                return uint8(255)
            if new_pix < 0:
                return uint8(0)
            return uint8(new_pix)

        table_gamma = [set_pix_gamma(pix) for pix in range(256)]
        vfunc_gamma = vectorize(lambda pix: table_gamma[int(pix)])

        self.preview_pixels[
        point_left_top[1]:point_right_bottom[1],
        point_left_top[0]:point_right_bottom[0]
        ] = vfunc_gamma(self.modify_pixels[
                        point_left_top[1]:point_right_bottom[1],
                        point_left_top[0]:point_right_bottom[0]].copy())

    def accept_change(self):
        self.modify_pixels = self.preview_pixels.copy()
