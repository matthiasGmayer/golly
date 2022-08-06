import importlib
import numpy as np
import npg
import optimize
import golly as g
from negentropy import *

importlib.reload(npg)
importlib.reload(optimize)

name = "num_cells/best_worst"
best_opts = np.load(f"data/{name}_best_opts.npy")
worst_opts = np.load(f"data/{name}_worst_opts.npy")
best_boards = np.load(f"data/{name}_best_boards.npy")
worst_boards = np.load(f"data/{name}_worst_boards.npy")
npg.start_board(width=100, height=100)
# for o, b in worst:
#     npg.set_board(b)
#     g.update()
#     npg.set_board(npg.get_board())

index, opt = max(enumerate(best_opts), key=lambda x: x[0])
board = best_boards[index]
npg.set_board(board)
g.update()

# width, height = 10, 10
# npg.start_board(width=width, height=height)
# shape = width, height
# board = np.array([1] * 10 + [0] * 90).reshape(shape)
# npg.log(board)
# npg.set_board(board)
# g.update()
# npg.log(npg.get_board())
# npg.set_board(npg.get_board())

# negentropy = NumberOfCells([0, 0, 0, 0], [0, 0, 100, 100])
# negentropy.save_board()
# g.autoupdate(True)
# optimize.run_until_converge()
# npg.show(m[0], negentropy.get_optimization())
