import pygame as pg
import os

vec = pg.math.Vector2

start = 0

class textBox:
    def __init__(self, x, y, width, height, bgColor=(20, 20, 20), activeColor=(0, 0, 0), textColor=(0, 255, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = vec(x, y)
        self.size = vec((width, height))
        self.image = pg.Surface((width, height))
        self.bgColor = bgColor
        self.activeColor = activeColor
        self.active = False
        self.text = ""
        self.textColor = textColor
        self.font = pg.font.SysFont("Consolas", 15)
        self.consoleText = "System32> "

    def update(self):
        pass

    def draw(self, window):
        if not self.active:
            self.image.fill(self.bgColor)
            text = self.font.render(self.consoleText + self.text, False, self.textColor)
            textHeight = text.get_height()
            self.image.blit(text, (0, (self.height-textHeight)))
        else:
            self.image.fill(self.activeColor)
            text = self.font.render(self.consoleText + self.text, False, self.textColor)
            textHeight = text.get_height()
            self.image.blit(text, (0, (self.height-textHeight)))
        window.blit(self.image, self.pos)

    def addText(self, key):
            if 31 < key < 127:
                text = list(self.text)
                text.append(chr(key))
                self.text = ''.join(text)
            elif key == 13:
                print(self.text)
                if self.text == ("start radar"):
                    os.system('cmd /c "start radar.py"')
                self.text = ''
            elif key == 271:
                print(self.text)
                if self.text == ("start radar"):
                    os.system('cmd /c "start radar.py"')
                self.text = ''
            elif key == 8:
                try:
                    text = list(self.text)
                    text.pop()
                    self.text = ''.join(text)
                except:
                    pass


    def checkClick(self, pos):
        if pos[0] > self.x and pos[0] < self.x+self.width:
            if pos[1] > self.y and pos[1] < self.y+self.height:
                self.active = True
            else:
                self.active = False
        else:
            self.active = False