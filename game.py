import tkinter as tk
import game_logic as gl
import threading
import time


# wall: w
# player: number
# explodable wall: e
# bomb: b
# power-up: u
# free: f
class Game:
    # menu variables
    title_label = None
    real_player_frame = None
    real_player_label = None
    real_player_entry = None
    ai_player_frame = None
    ai_player_label = None
    ai_player_entry = None
    button_frame = None
    play_button = None
    exit_button = None
    # board variables
    board_canvas = None
    row_num = 0
    col_num = 0
    # GameLogic
    game_logic = None

    player_colors = ["#e6194b", "#f58231", "#ffe119", "#808000", "#3cb44b", "#42d4f4", "#4363d8", "#911eb4", "#f032e6", "#a9a9a9"]

    def __init__(self):

        self.window = tk.Tk()

        self.row_size = 50
        self.col_size = 81
        self.window.title('BOMBERMAN')
        # self.window.minsize(self.col_num*self.col_size+10, self.row_num*self.row_size+10)
        self.menu_frame = tk.Frame(master=self.window, width=self.col_num * self.col_size + 10,
                                   height=self.row_num * self.row_size + 10)
        self.board_frame = tk.Frame(master=self.window, width=self.col_num * self.col_size + 10,
                                    height=self.row_num * self.row_size + 10)
        self.__refresher = threading.Thread(target=self.__refresh)
        self.build_menu()


        # self.__refresher.start()

        self.window.mainloop()

    def __refresh(self):
        while True:
            self.build_board()
            time.sleep(0.1)

    def start(self):
        self.game_logic = gl.GameLogic(int(self.real_player_entry.get()), int(self.ai_player_entry.get()), './maps/map_test.txt')
        self.__refresher.start()


    def build_menu(self):

        self.title_label = tk.Label(master=self.menu_frame, text="BOMBERMAN", font=("Roboto", 25))
        self.real_player_frame = tk.Frame(master=self.menu_frame)
        self.real_player_label = tk.Label(master=self.real_player_frame, text='Number of real players')
        self.real_player_entry = tk.Entry(master=self.real_player_frame,
                                          textvariable=tk.StringVar(master=self.real_player_entry, value="1"))
        self.ai_player_frame = tk.Frame(master=self.menu_frame)
        self.ai_player_label = tk.Label(master=self.ai_player_frame, text="Number of AI players", )
        self.ai_player_entry = tk.Entry(master=self.ai_player_frame,
                                        textvariable=tk.StringVar(master=self.ai_player_entry, value="3"))
        self.button_frame = tk.Frame(master=self.menu_frame)
        self.play_button = tk.Button(master=self.button_frame, text='PLAY', command=self.start)
        self.exit_button = tk.Button(master=self.button_frame, text='EXIT', command=self.window.destroy)
        self.title_label.pack()
        self.real_player_label.pack()
        self.real_player_entry.pack()
        self.real_player_frame.pack(side=tk.LEFT, padx=100, pady=100)
        self.ai_player_label.pack()
        self.ai_player_entry.pack()
        self.ai_player_frame.pack(side=tk.RIGHT, padx=100, pady=100)
        self.play_button.pack(pady=15)
        self.exit_button.pack(side=tk.BOTTOM)
        self.button_frame.pack(side=tk.BOTTOM, padx=100, pady=100)
        self.menu_frame.grid(column=0, row=0)

    def build_board(self):

        self.row_num = len(self.game_logic.get_game_board())
        self.col_num = len(self.game_logic.get_game_board()[0])

        self.board_frame = tk.Frame(master=self.window)
        self.board_canvas = tk.Canvas(self.board_frame, width=self.col_num * self.col_size,
                                      height=self.row_num * self.row_size)
        self.board_canvas.pack()
        for i in range(self.col_num):
            for j in range(self.row_num):
                x1 = i * self.col_size
                x2 = (i + 1) * self.col_size
                y1 = j * self.row_size
                y2 = (j + 1) * self.row_size
                if self.game_logic.get_game_board()[j][i] == "w":
                    self.board_canvas.create_rectangle(x1, y1, x2, y2, fill="#000000", outline="#000000")
                elif self.game_logic.get_game_board()[j][i] == "f":
                    self.board_canvas.create_rectangle(x1, y1, x2, y2, fill="grey", outline="#000000")
                elif self.game_logic.get_game_board()[j][i] == "e":
                    self.board_canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="#000000")
                elif self.game_logic.get_game_board()[j][i] == "b":
                    self.board_canvas.create_rectangle(x1, y1, x2, y2, fill="grey", outline="#000000")
                    self.board_canvas.create_rectangle(x1 + 15, y1 + 15, x2 - 15, y2 - 15, fill="black",
                                                       outline="black")
                elif "b" in str(self.game_logic.get_game_board()[j][i]):
                    self.board_canvas.create_rectangle(x1, y1, x2, y2, fill="grey", outline="#000000")
                    self.board_canvas.create_rectangle(x1 + 15, y1 + 3, x2 - 15, y2 - 27, fill="black", outline="black")
                    self.board_canvas.create_rectangle(x1 + 15, y1 + 28, x2 - 15, y2 - 2, fill=self.player_colors[int(self.game_logic.get_game_board()[j][i][0])],
                                                       outline=self.player_colors[int(self.game_logic.get_game_board()[j][i][0])])
                else:
                    self.board_canvas.create_rectangle(x1, y1, x2, y2, fill="grey", outline="#000000")
                    self.board_canvas.create_rectangle(x1 + 15, y1 + 15, x2 - 15, y2 - 15, fill=self.player_colors[int(self.game_logic.get_game_board()[j][i])],
                                                       outline=self.player_colors[int(self.game_logic.get_game_board()[j][i])])

        self.board_frame.grid(column=0, row=0)


game = Game()
