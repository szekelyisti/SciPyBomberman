#wall: w
#player: p
#explodable wall: e
#bomb: b
#power-up: u
#free: f

from tkinter import *
import random

class GameBoard:
    row_num = 11
    col_num = 13
    row_size = 50
    col_size = 50
    board = []

    def __init__(self, map):
        with open(map) as f:
            self.board = f.read().splitlines()
        self.window = Tk()
        self.window.title("Bomber-man")
        self.canvas = Canvas(self.window, width=self.col_num*self.col_size, height=self.row_num*self.row_size)
        self.canvas.pack()

        #self.window.bind("<Key>", self.key_input)
        #self.window.bind("<Button-1>", self.mouse_input)

    def draw(self):
        for i in range(self.col_num):
            for j in range(self.row_num):
                x1 = i*self.col_size
                x2 = (i+1)*self.col_size
                y1 = j*self.row_size
                y2 = (j+1)*self.row_size
                if self.board[j][i] == "w":
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="#000000")
                elif self.board[j][i] == "f":
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="green", outline="#000000")
                elif self.board[j][i] == "e":
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="#000000")

    def mainloop(self):
        while True:
            self.window.update()
            self.draw()
