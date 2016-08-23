import tkinter as tk

class GUI:
	def __init__(self, core):
		self.core = core
		self.height, self.width = 400, 400
		self.grid = self.height / 10
		self.root = self.game.window

		self.make_canvas()
		self.root.mainloop()

		def make_canvas(self):
			self.map = tk.Canvas(self.root, height=self.height, width=self.width)
			self.map.bind('<Button-1>', self.mouse_click)
			self.map.grid(row=0, column=0)

			self.load_map(self.core.grid, self.map)

		def mouse_click(self, event):
			if not self.end:
				mouse_row = int(event.y // self.grid) 
				mouse_col = int(event.x // self.grid)

				self.core.drop_token(mouse_row, mouse_col, self.core.grid)

				self.load_map(self.core.grid, self.map)

		def load_map(self, grid, map):
			self.grid = grid
			self.map = map
			self.map.delete('all')

			# Draws the grid
			for i in range(len(grid)):
				self.map.create_line(0, i * self.grid, len(grid) * self.grid, i * self.grid)
				self.map.create_line(i * self.grid, 0, i * self.grid, len(grid) * self.grid)

			# Draws the tokens:
			for i in range(len(grid)):
				for j in range(len(grid)):
					if grid[i][j].sign == "0":
						pass
					elif grid[i][j].sign == "1":
						colour = "blue"
					elif grid[i][j].sign == "2":
						colour = "red"