# Gravity Connect
A connect-4 like game

## How to run
If running from source code, you will need Python 3 and tkinter library, which is probably bundled with you python installation.
Simply run the main.py file and the game should work.

### When running on Windows 8 or Windows 10:
When running windows binary builds of this game on Windows 8 or 10, windows smartscreen will probably block the program. To bypass this, click more info in the windows smartscreen dialog and a new button with something like "run anyway" on it will appear. Just click it and the program should start normally. If you are not admin, you will also need admin's password to do this.

## How to play
The game is very simple and similar to connect-4. The goal is to make a row of four tokens of your color. The main difference is that in regular connect-4 the tokens fall down, while in our game tokens fall in four directions, depending on where the token was placed. It will fall left if it was put on the left quarter of the board, down if it was put on the bottom quarter of the board... 

There are also special fields colored grey on the borders between quarters. Tokens placed on those fields will stay there and won't fall in any direction. Four yellow fields in the middle are blocked - you can't put tokens on them.

