import importlib
import time
import numpy as np
import npg
import optimize
import golly as g
import negentropy

importlib.reload(npg)
importlib.reload(optimize)
importlib.reload(negentropy)
from negentropy import *


def visualize(dir, negentropy, width, height, quality="best"):
    opts = np.load(f"data/{dir}/{quality}_opts.npy")
    boards = np.load(f"data/{dir}/{quality}_boards.npy")
    npg.start_board(width=width, height=height)

    # index, opt = max(enumerate(best_opts), key=lambda x: x[0])
    # board = best_boards[index]
    # index, opt = min(enumerate(worst_opts), key=lambda x: x[0])
    # board = worst_boards[index]

    for board in boards:
        npg.set_board(board)
        # npg.show(opt)
        g.update()
        time.sleep(0.5)
        g.autoupdate(True)
        optimize.run_until_converge(negentropy, on_run=npg.show)
        time.sleep(0.5)
        g.autoupdate(False)
        # npg.show(opt, negentropy.get_optimization())


w, h = 100, 100
w2, h2 = w // 2, h // 2

# dir = "num_cells_left_right"
# negentropy = negentropy.load_negentropy("left_right_w100h100")

dir = "num_cells"
negentropy = NumberOfCells([0, 0, 0, 0], [0, 0, w, h])

quality = "best"
# quality = "worst"
visualize(dir, negentropy, w, h, quality)
# dir = "num_cells"
