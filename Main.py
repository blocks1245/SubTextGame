import pygame as pg
import sys

from TextBoxClass import *
from Commands import *


pg.init()
window = pg.display.set_mode((1000, 750))

textBoxes = []
textBoxes.append(textBox(350, 600, 300, 150))


pg.display.set_caption("Sub Game")

width, height = pg.display.get_surface().get_size()

running = True
while running:
    # Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            for box in textBoxes:
                box.checkClick(pg.mouse.get_pos())
        if event.type == pg.KEYDOWN:
            for box in textBoxes:
                if box.active:
                    box.addText(event.key)

    # Update


    # Draw
    window.fill((54, 54, 54))

    for box in textBoxes:
        box.draw(window)

    pg.display.flip()