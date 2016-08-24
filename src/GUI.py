import tkinter as tk
from constants import * 

class GUI:
    def __init__(self, core):
        self.core = core
        self.height, self.width = FRAMESIZE, FRAMESIZE
        self.grid = self.height / 10
        self.root = tk.Tk()
        
        self.turn = True
        
        self.make_canvas()
        self.root.mainloop()

    def make_canvas(self):
        self.map = tk.Canvas(self.root, height=self.height, width=self.width)
        self.map.bind('<Button-1>', self.mouse_click)
        self.map.grid(row=0, column=0)

        self.load_map(self.core.grid, self.map)

    def mouse_click(self, event):
        if not self.core.end():
            mouse_row = int(event.y // self.grid) 
            mouse_col = int(event.x // self.grid)
            
            if self.valid_coords(mouse_row, mouse_col):
                self.drop_token(mouse_row, mouse_col)
                if self.turn:
                    sign = 1
                else:
                    sign = 2
                self.core.insert_token(mouse_row, mouse_col, sign)
                self.turn = not self.turn
                
                self.load_map(self.core.grid, self.map)

    def load_map(self, grid, map):
        self.map = map
        self.map.delete('all')
        # Dhonraws the grid
        for i in range(len(grid)):
            self.map.create_line(0, i * self.grid, TABLESIZE * self.grid, i * self.grid)
            self.map.create_line(i * self.grid, 0, i * self.grid, TABLESIZE * self.grid)

        # Draws the tokens and special fields:
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j].sign == 0:
                    pass
                elif grid[i][j].sign == 1:
                    colour = "blue"
                elif grid[i][j].sign == 2:
                    colour = "red"
                    
                if grid[i][j].is_special:
                    colour = "gray"
                    self.map.create_rectangle(i * self.grid, j * self.grid,
                                              (i + 1) * self.grid, (j + 1) * self.grid, fill=colour)

    def drop_token(self, x, y):
        pos = self.core.get_token_pos(x, y)
        move_dir = self.core.grid[x][y].where_is()
        print("x: ", x, "y: ", y)
        print("pos ", pos)
        print("move_dir ", move_dir)
        while (x != pos[0]) and (y != pos[1]):
            if self.turn:
                colour = "blue"
            else:
                colour = "red"
                
            self.map.create_rectangle(x * self.grid, y * self.grid,
                                      (x + 1) * self.grid, (y + 1) * self.grid, fill=colour)
            x += move_dir[0]
            y += move_dir[1]
                
    def valid_coords(self, x, y):
        return True
                                                        
