import tkinter as tk

class MainMenu:

    def __init__(self, _width=800, _height=800, _real_player_num=1, _ai_player_num=1):
        self.game = None
        self.play_button = None
        self.ai_player_frame = None
        self.real_player_frame = None
        self.title_label = None
        self.canvas = None
        self.ai_player_label = None
        self.real_player_entry = None
        self.ai_player_entry = None
        self.real_player_label = None
        self.frame = None
        self.real_player_num = _real_player_num
        self.ai_player_num = _ai_player_num
        self.width = _width
        self.height = _height

        #self.draw()

    def draw(self):
        self.frame = tk.Frame(master=self.game.window)
        self.title_label = tk.Label(master=self.frame, text="BOMBERMAN", font=("Roboto", 25))

        self.real_player_frame = tk.Frame(master=self.frame)
        self.real_player_label = tk.Label(master=self.real_player_frame, text="Real player number")
        self.real_player_entry = tk.Entry(master=self.real_player_frame,
                                          textvariable=tk.StringVar(master=self.game.window, value="1"))
        self.ai_player_frame = tk.Frame(master=self.frame)
        self.ai_player_label = tk.Label(master=self.ai_player_frame, text="AI player number", )
        self.ai_player_entry = tk.Entry(master=self.ai_player_frame,
                                        textvariable=tk.StringVar(master=self.game.window, value="3"))
        self.play_button = tk.Button(master=self.frame, text='PLAY', command=self.game.start_game)

        self.title_label.pack()
        self.real_player_label.pack()
        self.real_player_entry.pack()
        self.real_player_frame.pack(side=tk.LEFT)
        self.ai_player_label.pack()
        self.ai_player_entry.pack()
        self.ai_player_frame.pack(side=tk.RIGHT)
        self.play_button.pack(side=tk.BOTTOM)

    def set_game(self, _game):
        self.game = _game
