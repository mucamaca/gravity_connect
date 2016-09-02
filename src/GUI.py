import tkinter as tk
from core import Core
from constants import *
from ai import minimax

class GUI:
    def __init__(self, core):
        self.core = core
        self.height, self.width = FRAMESIZE, FRAMESIZE
        self.cellsize = CELLSIZE
        self.root = tk.Tk()
        self.root.title("Gravity Connect")
        self.turn = True
        self.switch_id = 0
        self.mouse_x = 0
        self.mouse_y = 0
        
        self.make_canvas()

        self.root.mainloop()

    def make_canvas(self):
        self.map = tk.Canvas(self.root, height=self.height, width=self.width)
        self.map.bind('<Button-1>', self.mouse_click)
        self.map.grid(row = 0, column = 0)

        self.load_map() 

    def load_map(self):
            self.map.delete('all')
            # Draws the grid
            for i in range(TABLESIZE):
                self.map.create_line(
                    0, i * self.cellsize, TABLESIZE * self.cellsize,
                    i * self.cellsize
                )
                self.map.create_line(
                    i * self.cellsize, 0, i * self.cellsize,
                    TABLESIZE * self.cellsize
                )

            # Draws the tokens and special fields:
            for i in range(TABLESIZE):
                for j in range(TABLESIZE):
                    if Core.is_special(i, j):
                        colour = "gray"
                    else:
                        colour = "white"
                    if self.core.grid[i][j] == 1:
                        colour = COLOUR_1
                    if self.core.grid[i][j] == 2:
                        colour = COLOUR_2
                    self.map.create_rectangle(
                        i * self.cellsize, j * self.cellsize,
                        (i + 1) * self.cellsize,
                        (j + 1) * self.cellsize, fill=colour
                    )

    def mouse_click(self, event):
        self.mouse_x = int(event.x // self.cellsize) 
        self.mouse_y = int(event.y // self.cellsize)
        
        if self.core.valid_coords(self.mouse_x, self.mouse_y):
            self.drop_token(self.mouse_x, self.mouse_y,
                            self.core.get_token_pos(self.mouse_x, self.mouse_y))
            self.root.after(self.increment_id(self.mouse_x, self.mouse_y) * 250,
                            self.place_token, self.mouse_x, self.mouse_y)

        
        # coords = minimax(self.core, self.turn, MAXDEPTH)
        # self.drop_token(coords[0], coords[1], self.core.get_token_pos(coords[0], coords[1]))
        # self.root.after(self.increment_id(coords[0], coords[1]) * 250,
        #                 self.place_token, coords[0], coords[1])
        # self.turn = not self.turn
    def drop_token(self, x, y, pos):
        move_dir = Core.where_is(x, y)
        if (x, y) != pos:
            if self.turn:
                colour = COLOUR_1
            else:
                colour = COLOUR_2
            
            self.load_map()
            self.map.create_rectangle(
                x * self.cellsize, y * self.cellsize,
                (x+1) * self.cellsize, (y+1) * self.cellsize, fill=colour
            )
            
            x += move_dir[0]
            y += move_dir[1]

            self.root.after(250, self.drop_token, x, y, pos)

    def increment_id(self, x, y):
        pos = self.core.get_token_pos(x, y)
        if x == pos[0]:
            diff = abs(y - pos[1])
        else:
            diff = abs(x - pos[0])
        self.switch_id = diff
        return self.switch_id

    def place_token(self, x, y):
        pos = self.core.get_token_pos(x, y)
        sign = (not self.turn) + 1
        self.core.insert_token(pos[0], pos[1], sign)
        if (x, y) == pos:
            self.core.valid_list.remove(pos)
        if self.core.end(*pos):
            self.game_end(sign)
        self.turn = not self.turn
        self.load_map()

    def game_end(self, sign):
        self.end_screen = tk.Tk()
        self.end_screen.protocol("WM_DELETE_WINDOW", self.quit_game)
        if sign:
            end_text = tk.Label(
                self.end_screen,
                text='Player wins!',
                font=('Helvetica', 16)
            )
        else:
            end_text = tk.Label(
                self.end_screen,
                text='The computer wins!',
                font=('Helvetica', 16)
            )

        text = tk.Label(self.end_screen,
                        text='Do you want to play again?')
        restart = tk.Button(self.end_screen, text='Yes!',
                            command=self.restart_game)
        g_exit = tk.Button(self.end_screen, text='No!',
                           command=self.quit_game)

        end_text.pack()
        text.pack(side=tk.LEFT)
        restart.pack(side=tk.LEFT)
        g_exit.pack(side=tk.LEFT)

    def restart_game(self):
        # it restarts the game
        self.end_screen.destroy()
        self.root.destroy()
        del self.core
        main()

    def quit_game(self):
        # it destroys both screens
        self.end_screen.destroy()
        self.root.destroy()

def main():
    core = Core()
    gui = GUI(core)

def do_nothing():
    pass
