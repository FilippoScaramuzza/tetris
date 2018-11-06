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
CANVASDIMX, CANVASDIMY = 200, 400
ROWS = 20
COLS = 10
sqsize = CANVASDIMX // COLS
sqsizeOffset = 1
spawnable = True
selected = 0

blockSprites = g2d.load_image("media/blocks.png")
#background = (0, 38, 102)
#lines = (0, 88, 102)
background = (10, 10, 10)
lines = (50, 50, 50)
frameCounter = 0

#blocks
pixelsize = sqsize

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
board = []

#functions

def drawBlocks():

	for b in blockList:
		relx = b._x * sqsize
		rely = b._y * sqsize
		
		for r in range(0, 4):
			for c in range(0, 4):
				if b._cells[r][c] == 1:
					g2d.draw_image_clip(blockSprites, (relx, rely, sqsize, sqsize), (b._type * sqsize, 0, pixelsize, pixelsize))
				relx += pixelsize
			rely += pixelsize
			relx = b._x * sqsize

def updateBoard():
	global board, spawnable

	board = [[0 for i in range(COLS)] for j in range(ROWS)]

	for b in blockList:
		for r in range(ROWS):
			for c in range(COLS):
				if b._y in range(r - 3, r + 1) and b._x in range(c - 3, c + 1):
					if b._cells[r - b._y][c - b._x] == 1:
						print(b._cells)
						board[r][c] = 1
				""" i += 1
			j += 1
			i = 0 """

		checkStop()

def checkStop():
	global spawnable
	
	for b in blockList:
		for i in range(4):
			for _j in range(4):
				if b._cells[i].count(1) == 0:
					print(b._cells[i])
					if b._y + 3 == ROWS - 1:
						b._ismoving = False
						if b._id == selected:
							spawnable = True
				else:
					if b._y + 3 == ROWS:
						b._ismoving = False
						if b._id == selected:
							spawnable = True

def update():
	global spawnable, frameCounter, selected

	if frameCounter %  5 == 0:
		if spawnable:
			blockList.append(Block(randint(0, 6), randint(0, 6), -3))
			selected = blockList[len(blockList) - 1]._id
			spawnable = False

		init_background()
		checkStop()
		move(blockList)
		updateBoard()
		drawBlocks()
		for i in range(ROWS):
			for j in range(COLS):
				print(board[i][j], end=" ")
			print("")
		
		print("==================")

	frameCounter += 1


def init_background():
    for r in range(ROWS):
        for c in range(COLS):
            g2d.draw_rect(lines, (c * sqsize, r * sqsize, sqsize, sqsize))
            g2d.draw_rect(background, (c * sqsize + sqsizeOffset, r * sqsize + sqsizeOffset, sqsize - sqsizeOffset * 2, sqsize - sqsizeOffset * 2))

def main():
	global board
	g2d.init_canvas((CANVASDIMX, CANVASDIMY))
	init_background()

	""" blockList.append(Block(0, 6, 5))
	blockList.append(Block(1, 2, 16))
	blockList.append(Block(2, 6, 8))
	blockList.append(Block(3, 6, 1))
	blockList.append(Block(4, 2, 11))
	blockList.append(Block(5, 1, 1))
	blockList.append(Block(6, 6, 13)) """

	board = [[0 for i in range(COLS)] for j in range(ROWS)]
	g2d.main_loop(update, 1000 // 20)

main()