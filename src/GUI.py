#!/usr/bin/python3

import tkinter as tk
from core import Core
#from constants import *
#from ai import minimax


class GUI:
    c = 1
    def __init__(self):
        self.core = Core()
        self.height, self.width = FRAMESIZE, FRAMESIZE
        self.cellsize = CELLSIZE
        self.root = tk.Tk()
        self.root.title("Gravity Connect")
        self.turn = True

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
                    colour = [BG_COLOUR, COLOUR_1, COLOUR_2, SPECIAL_COLOUR][self.core.grid[i][j]]
                    if colour == BG_COLOUR and Core.is_special(i, j):
                        colour = SPECIAL_COLOUR
                    self.map.create_rectangle(
                        i * self.cellsize, j * self.cellsize,
                        (i + 1) * self.cellsize,
                        (j + 1) * self.cellsize, fill=colour
                    )

    def mouse_click(self, event):
        self.load_map()
        mouse_x = int(event.x // self.cellsize)
        mouse_y = int(event.y // self.cellsize)

        if self.core.valid_coords(mouse_x, mouse_y):
            self.place_token(mouse_x, mouse_y)
            #self.drop_token(mouse_x, mouse_y,
            #                self.core.get_token_pos(mouse_x, mouse_y))
            #self.root.after(self.increment_id(mouse_x, mouse_y) * 250,
            #                self.place_token, mouse_x, mouse_y)

            if self.c %2:
                print("calculating...")
                coords = minimax(self.core, self.turn, MAXDEPTH, 0, 0)
                print(coords[2], coords[1])
            self.c += 1
            # self.drop_token(coords[1], coords[2],
            #                 self.core.get_token_pos(coords[1], coords[2]))
            # self.root.after(self.increment_id(coords[1], coords[2]) * 250,
            #                 self.place_token, coords[1], coords[2])
            for i in self.core.grid:
                print(i)

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
            return abs(y - pos[1])
        else:
            return abs(x - pos[0])


    def place_token(self, x, y):
        pos = self.core.get_token_pos(x, y)
        self.core.insert_token(pos[0], pos[1], self.turn)
        self.load_map()
        if (x, y) == pos:
            self.core.valid_list.remove(pos)
        if self.core.end(*pos):
            self.game_end()
        self.turn = not self.turn
        print(self.core.score())

    def game_end(self):
        self.end_screen = tk.Tk()
        self.end_screen.protocol("WM_DELETE_WINDOW", self.quit_game)
        if self.turn + 1 == PLAYER_SIGN:
            end_text = tk.Label(
                self.end_screen,
                text='Player wins!',
                font=('Helvetica', 16)
            )
        elif self.turn + 1 == COMPUTER_SIGN:
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
        self.__init__()

    def quit_game(self):
        # it destroys both screens
        self.end_screen.destroy()
        self.root.destroy()

def main():
    gui = GUI()

def do_nothing():
    pass

if __name__ == "__main__":
    main()
