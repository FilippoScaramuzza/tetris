'''
===TETRIS===

By Filippo Scaramuzza
Università degli Studi di Parma

'''

#libraries
import g2d
from blocks import Block, move
from random import randint

#variables and costants
CANVASDIMX, CANVASDIMY = 400, 800
ROWS = 20
COLS = 10
sqsize = CANVASDIMX // COLS
sqsizeOffset = 1
spawnable = True

blockSprites = g2d.load_image("media/blocks.png")
#background = (0, 38, 102)
#lines = (0, 88, 102)
background = (10, 10, 10)
lines = (50, 50, 50)

#blocks
pixelsize = 40

''''
blocks = [0, 1, 2, 3, 4, 5, 6]
#         |  |  |  |  |  |  |
#      Line  |  |  |  |  |  |
#           L1  |  |  |  |  |
#              L2  |  |  |  |
#             square  |  |  |
#                   _ |  |  |
#                "_| "   |  |
#                        |  |
#                   podium  |
#                       _   |
#                      " |_"|
'''
blockList = []

#functions

def drawBlocks():
	for b in blockList:
		relx = b._x * sqsize
		rely = b._y * sqsize
		absx = relx - 2 * sqsize
		absy = rely - 1 * sqsize
		
		for r in range(0, 4):
			for c in range(0, 4):
				if b._cells[r][c] == 1:
					g2d.draw_image_clip(blockSprites, (absx, absy, sqsize, sqsize), (b._type * sqsize, 0, pixelsize, pixelsize))
				absx += pixelsize
			absy += pixelsize
			absx = relx - 2 * sqsize

def update():
	global spawnable

	if spawnable:
		blockList.append(Block(randint(0, 6), randint(2, 8), -3))
		spawnable = False

	init_background()
	move(blockList)
	drawBlocks()


def init_background():
    for r in range(ROWS):
        for c in range(COLS):
            g2d.draw_rect(lines, (c * sqsize, r * sqsize, sqsize, sqsize))
            g2d.draw_rect(background, (c * sqsize + sqsizeOffset, r * sqsize + sqsizeOffset, sqsize - sqsizeOffset * 2, sqsize - sqsizeOffset * 2))

def main():
	g2d.init_canvas((CANVASDIMX, CANVASDIMY))
	init_background()
	""" blockList.append(Block(0, 6, 5))
	blockList.append(Block(1, 2, 16))
	blockList.append(Block(2, 6, 8))
	blockList.append(Block(3, 6, 1))
	blockList.append(Block(4, 2, 11))
	blockList.append(Block(5, 1, 1))
	blockList.append(Block(6, 6, 13)) """
	g2d.main_loop(update, 1000)

main()