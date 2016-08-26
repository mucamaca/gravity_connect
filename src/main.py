from core import Core
from GUI import GUI
from ai import AI

if __name__ == "__main__":
    core = Core()
    ai = AI(core)
    gui = GUI(core, ai)
