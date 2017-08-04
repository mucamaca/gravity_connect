#!/usr/bin/python3

import tkinter as tk
from core import Core
from gameconfig import config
#from ai import minimax


class GUI:
    c = 1
    def __init__(self):
        self.core = Core()
        self.grid = self.core.grid
        self.height, self.width = 400, 400
        self.tablesize = 10
        self.cellsize = 40

        self.colour_list = [config.colour_1, config.colour_2, config.colour_3, config.colour_4, config.colour_bg, config.colour_special]

        self.lock_click = False
        self.root = tk.Tk()
        self.root.title("Gravity Connect")

        # indicates which player is on the move (0-n), special number for ai?
        self.turn = 0


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
            for i in range(self.tablesize):
                self.map.create_line(
                    0, i * self.cellsize, self.tablesize * self.cellsize,
                    i * self.cellsize
                )
                self.map.create_line(
                    i * self.cellsize, 0, i * self.cellsize,
                    self.tablesize * self.cellsize
                )

            # Draws the tokens and special fields:
            for i in range(self.tablesize):
                for j in range(self.tablesize):
                    colour = self.colour_list[self.core.grid[i][j].state]
                    self.map.create_rectangle(
                        i * self.cellsize, j * self.cellsize,
                        (i + 1) * self.cellsize,
                        (j + 1) * self.cellsize, fill=colour
                    )

    def mouse_click(self, event):
        self.load_map()
        mouse_x = int(event.x // self.cellsize)
        mouse_y = int(event.y // self.cellsize)

        if self.core.can_insert(mouse_x, mouse_y):
            self.place_token(mouse_x, mouse_y)

        # This block is for AI and is not part of v0.2.x
        #
        # if self.c %2:
        #     self.lock_click = True
        #     print("calculating...")
        #     coords = minimax(self.core, self.turn, MAXDEPTH, 0, 0)
        #     self.place_token(*coords)
        # self.c += 1


    def drop_token(self, x, y, pos):
        move_dir = self.grid[x][y].dir
        # recursively drops the token
        if (x, y) != pos:
            colour = self.colour_list[self.turn]

            self.load_map()
            self.map.create_rectangle(
                x * self.cellsize, y * self.cellsize,
                (x+1) * self.cellsize, (y+1) * self.cellsize, fill=colour
            )

            x += move_dir[0]
            y += move_dir[1]

            self.root.after(250, self.drop_token, x, y, pos)
        else:
            self.core.insert_token(*pos)
            if self.grid.check_win():
               self.game_end()

    # This code is probably not needed anymore
    # def increment_id(self, x, y):
    #     pos = self.grid.get_token_pos(x, y)
    #     if x == pos[0]:
    #         return abs(y - pos[1])
    #     else:
    #         return abs(x - pos[0])


    def place_token(self, x, y):
        pos = self.grid.get_token_pos(x, y)
        pos = (pos[0], pos[1])
        self.lock_click = True
        self.drop_token(x, y, pos)
        self.load_map()
        self.lock_click = False
        self.turn = (self.turn + 1) % config.num_of_players


    def game_end(self):
        self.end_screen = tk.Tk()
        self.end_screen.protocol("WM_DELETE_WINDOW", self.quit_game)
        end_text = tk.Label(
            self.end_screen,
            text='Player {} wins!'.format(self.turn),
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


if __name__ == "__main__":
    gui = GUI()
