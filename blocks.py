'''
Blocks
'''

from random import randint
from uuid import uuid4

class Block:
    def __init__(self, type: int, x: int, y: int):
        self._id = uuid4()
        self._type = type #it's the color too
        self._cells = []
        self._x = x
        self._y = y
        self._ismoving = True
        self.populateBlock()

    def populateBlock(self):
        if self._type == 0:
            self._cells = [[0, 0, 0, 0],
                           [1, 1, 1, 1],
                           [0, 0, 0, 0],
                           [0, 0, 0, 0]]
            return
        
        if self._type == 1:
            self._cells = [[0, 0, 0, 0],
                           [0, 1, 1, 1],
                           [0, 0, 0, 1],
                           [0, 0, 0, 0]]
            return

        if self._type == 2:
            self._cells = [[0, 0, 0, 0],
                           [0, 1, 1, 1],
                           [0, 1, 0, 0],
                           [0, 0, 0, 0]]
            return
        
        if self._type == 3:
            self._cells = [[0, 0, 0, 0],
                           [0, 1, 1, 0],
                           [0, 1, 1, 0],
                           [0, 0, 0, 0]]
            return
        
        if self._type == 4:
            self._cells = [[0, 0, 0, 0],
                           [0, 0, 1, 1],
                           [0, 1, 1, 0],
                           [0, 0, 0, 0]]
            return
        
        if self._type == 5:
            self._cells = [[0, 0, 0, 0],
                           [0, 1, 1, 1],
                           [0, 0, 1, 0],
                           [0, 0, 0, 0]]
            return
        
        if self._type == 6:
            self._cells = [[0, 0, 0, 0],
                           [0, 1, 1, 0],
                           [0, 0, 1, 1],
                           [0, 0, 0, 0]]
            return
        
def move(blocks: list):
    for b in blocks:
        if b._ismoving:
            b._y += 1