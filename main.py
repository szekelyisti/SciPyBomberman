import board
import menu
import tkinter as tk


class Game:

    def __init__(self):
        self.window = tk.Tk()
        self.menu = menu.MainMenu()
        self.menu.set_game(self)
        self.board = board.GameBoard("./maps/map1.txt")
        self.board.set_game(self)

        self.menu.draw()
        self.menu.frame.pack()
        self.window.mainloop()

    def start_game(self):
        self.board.draw()
        self.board.frame.pack()



game = Game()
