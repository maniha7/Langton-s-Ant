import Pixel
import random
import time





class Ant():
    def __init__(self,screen,window,scaleFactor):
        self.x = 0
        self.y = 0
        self.scaleFactor = scaleFactor
        self.yMax = window.height // self.scaleFactor
        self.xMax = window.width // self.scaleFactor
        self.directionCounter = 0
        self.directions = ["UP","RIGHT","DOWN","LEFT"]
        self.direction = self.directions[0]
        self.screen=screen
        self.ant = Pixel.Pixel(self.screen,self.x,self.y)
        self.window = window
        self.updateColor = (0,0,0)

    def move(self):

        curPix = self.window.pixAtLocation(self.x,self.y)
        nextPix = self.nextInDirection(curPix)
        tempColor = (255,255,255)
        if self.getColor(nextPix)=="BLACK":
            self.changeDirection(self.RANDTURNS[0])
            tempColor = (self.COLOR1)
        elif self.getColor(nextPix)=="COLOR1":
            self.changeDirection(self.RANDTURNS[1])
            tempColor = (self.COLOR2)
        elif self.getColor(nextPix)=="COLOR2":
            self.changeDirection(self.RANDTURNS[2])
            tempColor = (self.COLOR3)
        elif self.getColor(nextPix)=="COLOR3":
            self.changeDirection(self.RANDTURNS[3])
            tempColor = (self.COLOR4)
        elif self.getColor(nextPix)=="COLOR4":
            self.changeDirection(self.RANDTURNS[4])
            tempColor = (self.COLOR2)
        elif self.getColor(nextPix)=="COLOR5":
            self.changeDirection(self.RANDTURNS[5])
            tempColor = (self.COLOR3)
        self.ant.draw((255, 255, 255), x=self.x, y=self.y)
        curPix.draw(self.updateColor,pix=curPix)
        self.updateColor = tempColor

    #turn left/right
    def changeDirection(self,way):
        if way=="RIGHT":
            if self.directionCounter <3:
                self.directionCounter +=1
            else:
                self.directionCounter = 0
            self.direction=self.directions[self.directionCounter]
        elif way =="LEFT":
            if self.directionCounter >0:
                self.directionCounter -=1
            else:
                self.directionCounter = 3
        self.direction=self.directions[self.directionCounter]

    #update future location and return next pixel in path
    def nextInDirection(self, curPix):
        if self.direction=="UP":
            if self.y+1 < self.yMax:
                self.y +=1
        elif self.direction=="DOWN":
            if self.y-1 >=0:
                self.y-=1
        elif self.direction=="LEFT":
            if self.x - 1 >= 0:
                self.x-=1
        elif self.direction=="RIGHT":
            if self.x + 1 < self.xMax:
                self.x+=1
        return Pixel.Pixel(self.screen,self.x,self.y)


    def getColor(self,pix):
        if self.screen.get_at((pix.x * self.scaleFactor, pix.y * self.scaleFactor))[:3] == self.COLOR1:
            return "COLOR1"
        if self.screen.get_at((pix.x * self.scaleFactor, pix.y * self.scaleFactor))[:3] == (0, 0, 0):
            return "BLACK"
        if self.screen.get_at((pix.x * self.scaleFactor, pix.y * self.scaleFactor))[:3] == self.COLOR2:
            return "COLOR2"
        if self.screen.get_at((pix.x * self.scaleFactor, pix.y * self.scaleFactor))[:3] == self.COLOR3:
            return "COLOR3"
        if self.screen.get_at((pix.x * self.scaleFactor, pix.y * self.scaleFactor))[:3] == self.COLOR4:
            return "COLOR4"
        if self.screen.get_at((pix.x * self.scaleFactor, pix.y * self.scaleFactor))[:3] == self.COLOR5:
            return "COLOR5"

    # color declarations
    def setColors(self,turns = None):
        random.seed(time.clock())
        MAXCOLORS = 5
        self.COLORS = []
        UPPERCOLORRANGES = [random.randrange(100, 255), random.randrange(100, 255), random.randrange(100, 255)]
        if turns == None:
            self.RANDTURNS = [random.randrange(0, 2), random.randrange(0, 2), random.randrange(0, 2), random.randrange(0, 2), random.randrange(0, 2), random.randrange(0, 2)]
        else: self.RANDTURNS = turns

        #prevent stuck starts
        if self.RANDTURNS[2] == self.RANDTURNS[3] and self.RANDTURNS[3] == self.RANDTURNS[4]:
            self.RANDTURNS[2] = not self.RANDTURNS[3]


        for i in range(len(self.RANDTURNS)):
            if self.RANDTURNS[i] == 1:
                self.RANDTURNS[i] = "RIGHT"
            else:
                self.RANDTURNS[i] = "LEFT"
    
        for x in range(MAXCOLORS):
            color = [0, 0, 0]
            for i in range(3):
                color[i] = random.randrange(UPPERCOLORRANGES[i] - 95, UPPERCOLORRANGES[i])
            color = tuple(color)
            self.COLORS.append(color)
        self.COLOR1 = self.COLORS[0]
        self.COLOR2 = self.COLORS[1]
        self.COLOR3 = self.COLORS[2]
        self.COLOR4 = self.COLORS[3]
        self.COLOR5 = self.COLORS[4]
