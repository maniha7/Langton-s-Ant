# A class containing info on a particular pixel on the screen at some given time
# Location, color, direction...
import pygame


class Pixel:

    # inits a matrix of all pixels, each pixel 4x4 real pixels (subject to change in scaleFactor var)
    def __init__(self, screen, x, y):
        self.scaleFactor = 4
        self.screenWidth, self.screenHeight = screen.get_size()
        self.screenWidth = self.screenWidth // self.scaleFactor
        self.screenHeight = self.screenHeight // self.scaleFactor
        self.x = x
        self.y = y
        self.screen = screen
        self.neighbors = []

    # RGB color
    def draw(self, color, x=0, y=0, pix=None):
        if pix is not None:
            pygame.draw.rect(self.screen, color,
                             (pix.x * self.scaleFactor, pix.y * self.scaleFactor, self.scaleFactor, self.scaleFactor))
        else:
            pygame.draw.rect(self.screen, color,
                             (x * self.scaleFactor, y * self.scaleFactor, self.scaleFactor, self.scaleFactor))

    # if pixel is touching the border, which border
    def isOnEdge(self, pixel):
        if pixel.x == 0 and pixel.y == 0: return "tlc"
        if pixel.x == 0 and pixel.y + 1 == self.screenHeight: return "blc"
        if pixel.x + 1 == self.screenWidth and pixel.y == 0: return "trc"
        if pixel.x + 1 == self.screenWidth and pixel.y + 1 == self.screenHeight: return "brc"
        if pixel.x == 0: return "left"
        if pixel.y == 0: return "top"
        if pixel.x + 1 == self.screenWidth: return "right"
        if pixel.y + 1 == self.screenHeight: return "bottom"
        return None
