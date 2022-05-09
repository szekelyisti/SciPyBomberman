# wall: w
# player: p
# explodable wall: e
# bomb: b
# power-up: u
# free: f

import tkinter as tk


class GameBoard:
    row_num = 11
    col_num = 13
    row_size = 50
    col_size = 50
    board = []

    def __init__(self, _map, _height=800, _width=800):
        self.game = None
        self.canvas = None
        self.frame = None
        self.width = _width
        self.height = _height

        with open(_map) as f:
            self.board = f.read().splitlines()
        #self.draw()

        # self.window.bind("<Key>", self.key_input)
        # self.window.bind("<Button-1>", self.mouse_input)

    def draw(self):
        self.frame = tk.Frame(master=self.game.window)
        self.canvas = tk.Canvas(self.frame, width=self.col_num * self.col_size,
                                height=self.row_num * self.row_size)
        self.canvas.pack()

        for i in range(self.col_num):
            for j in range(self.row_num):
                x1 = i * self.col_size
                x2 = (i + 1) * self.col_size
                y1 = j * self.row_size
                y2 = (j + 1) * self.row_size
                if self.board[j][i] == "w":
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="#000000")
                elif self.board[j][i] == "f":
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="green", outline="#000000")
                elif self.board[j][i] == "e":
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="#000000")

    def set_game(self, _game):
        self.game = _game

    # def mainloop(self):
    #    while True:
    #        self.window.update()
    #        self.draw()
