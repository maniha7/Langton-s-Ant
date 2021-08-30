import pygame
import Pixel
import Ant
import tkinter as tk

sysInfo = tk.Tk()

class window:
    def __init__(self):
        #init display settings
        pygame.init()
        pygame.display.set_caption("Langton's Ant")
        self.width = sysInfo.winfo_screenwidth()
        self.height = sysInfo.winfo_screenheight()
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.frozen = False
        self.color = (0,0,0)
        self.scaleFactor = 4

        #init pixel matrix
        self.pixels = {}
        self.cleanSlate()
        self.initAnt()






    def initAnt(self):
        self.ant = Ant.Ant(self.screen, self, self.scaleFactor)
        self.ant.setColors()
        self.ant.x = 240
        self.ant.y = 130


    #blank pixel setup
    def cleanSlate(self):
        for x in range(self.width//self.scaleFactor):
            for y in range(self.height//self.scaleFactor):
                cPix = Pixel.Pixel(self.screen,x,y)
                self.pixels[(x,y)]=cPix
                cPix.draw(self.color, x=x, y=y)


    #return current keyboard/mouse input
    def getEvent(self):
        return pygame.event.get()

    #Get pixel at x,y
    def pixAtLocation(self,x,y):
        pixel = self.pixels[(x,y)]
        return pixel

    # Start/Pause animation
    def freeze(self):
        self.frozen = not self.frozen

    #update screen graphics
    def update(self):
        self.ant.move()
        pygame.display.flip()

    #reset sim
    def reset(self):
        self.cleanSlate()
        self.initAnt()