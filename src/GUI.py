import tkinter as tk
from constants import *
from time import sleep

class GUI:
    def __init__(self, core):
        self.core = core
        self.height, self.width = FRAMESIZE, FRAMESIZE
        self.grid = self.height / TABLESIZE
        self.root = tk.Tk()
        self.turn = True
        
        self.make_canvas()

        self.root.mainloop()

    def make_canvas(self):
        self.map = tk.Canvas(self.root, height=self.height, width=self.width)
        self.map.bind('<Button-1>', self.mouse_click)
        self.map.grid(row = 0, column = 0)

        self.load_map() 

    def mouse_click(self, event):
        if self.core.end():
            return
        mouse_x = int(event.x // self.grid) 
        mouse_y = int(event.y // self.grid)
        
        if self.valid_coords(mouse_x, mouse_y):
            self.drop_token(mouse_x, mouse_y)
            sign = (not self.turn) + 1
            self.core.insert_token(mouse_x, mouse_y, sign)
            self.turn = not self.turn
            self.load_map()

    def load_map(self):
        self.map.delete('all')
        # Draws the grid
        for i in range(TABLESIZE):
            self.map.create_line(0, i * self.grid, TABLESIZE * self.grid, i * self.grid)
            self.map.create_line(i * self.grid, 0, i * self.grid, TABLESIZE * self.grid)

        # Draws the tokens and special fields:
        for i in range(TABLESIZE):
            for j in range(TABLESIZE):
                if self.core.grid[i][j].sign == 0:
                    colour = "white"
                if self.core.grid[i][j].is_special:
                    colour = "gray"
                if self.core.grid[i][j].sign == 1:
                    colour = COLOUR_1
                if self.core.grid[i][j].sign == 2:
                    colour = COLOUR_2
                self.map.create_rectangle(i * self.grid, j * self.grid,
                                        (i + 1) * self.grid, (j + 1) * self.grid, fill=colour)

    def drop_token(self, x, y):
        pos = self.core.get_token_pos(x, y)
        move_dir = self.core.grid[x][y].where_is()
        while (x != pos[0]) or (y != pos[1]):
            if self.turn:
                colour = COLOUR_1
            else:
                colour = COLOUR_2
            
            #self.load_map()
            self.map.create_rectangle(x * self.grid, y * self.grid,
                                      (x+1) * self.grid, (y+1) * self.grid, fill=colour)
            self.root.after(500, do_nothing())

            x += move_dir[0]
            y += move_dir[1]

                
    def valid_coords(self, x, y):
        return True
                                                        
def do_nothing():
    pass