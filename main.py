'''
===TETRIS===

By Filippo Scaramuzza
Università degli Studi di Parma

'''

#libraries
import g2d

#variables and costants
CANVASDIMX, CANVASDIMY = 400, 800
ROWS = 20
COLS = 10
sqsize = CANVASDIMX // COLS
sqsizeOffset = 1

#background = (0, 38, 102)
#lines = (0, 88, 102)
background = (10, 10, 10)
lines = (50, 50, 50)


#functions

def init_background():
    for r in range(ROWS):
        for c in range(COLS):
            g2d.draw_rect(lines, (c * sqsize, r * sqsize, sqsize, sqsize))
            g2d.draw_rect(background, (c * sqsize + sqsizeOffset, r * sqsize + sqsizeOffset, sqsize - sqsizeOffset * 2, sqsize - sqsizeOffset * 2))

def main():
    g2d.init_canvas((CANVASDIMX, CANVASDIMY))
    init_background()
    g2d.main_loop()

main()