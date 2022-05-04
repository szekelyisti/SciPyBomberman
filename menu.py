from tkinter import *

class MainMenu:

    def __init__(self, _real_player_num, _ai_player_num, _width, _height):
        self.real_player_num = _real_player_num
        self.ai_player_num = _ai_player_num

        self.window = Tk()
        self.window.title("Bomber-man")
        self.window.minsize(_width, _height)
        self.window.maxsize(_width, _height)
        self.canvas = Canvas(self.window, width=_width, height=_height)
        self.canvas.pack()
        self.title_label = Label(master=self.canvas, text="BOMBERMAN", font=("Roboto", 25))
        self.title_label.pack()
        self.player_frame = Frame(master=self.canvas)


        self.window.mainloop()