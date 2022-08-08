import importlib
import numpy as np
import npg
import optimize
import golly as g
import negentropy

importlib.reload(npg)
importlib.reload(optimize)
importlib.reload(negentropy)
from negentropy import *

dir = "num_cells"
best_opts = np.load(f"data/{dir}/best_opts.npy")
worst_opts = np.load(f"data/{dir}/worst_opts.npy")
best_boards = np.load(f"data/{dir}/best_boards.npy")
worst_boards = np.load(f"data/{dir}/worst_boards.npy")
w, h = 100, 100
w2, h2 = w // 2, h // 2
npg.start_board(width=w, height=h)
# for o, b in worst:
#     npg.set_board(b)
#     g.update()
#     npg.set_board(npg.get_board())

# index, opt = max(enumerate(best_opts), key=lambda x: x[0])
# board = best_boards[index]
# index, opt = min(enumerate(worst_opts), key=lambda x: x[0])
# board = worst_boards[index]
# for board in best_boards:
# for board in worst_boards:
#     npg.set_board(board)
#     # npg.show(opt)
#     negentropy = NumberOfCells([0, 0, 0, 0], [0, 0, 100, 100])
#     negentropy.save_board()
#     g.autoupdate(True)
#     optimize.run_until_converge()
#     g.autoupdate(False)
#     # npg.show(opt, negentropy.get_optimization())
#     npg.show(negentropy.get_optimization())

# width, height = 10, 10
# npg.start_board(width=width, height=height)
# shape = width, height
# board = np.array([1] * 10 + [0] * 90).reshape(shape)
# npg.log(board)
# npg.set_board(board)
# g.update()
# npg.log(npg.get_board())
# npg.set_board(npg.get_board())

negentropy = NumberOfCells([0, 0, 0, 0], [0, 0, 100, 100])
for i in range(100):
    board = (np.random.random((w, h)) > 1 / 2) + 0
    negentropy[board]

# negentropy = NumberOfCells([0, 0, w2, h], [w2, 0, w2, h])
negentropy = load_negentropy("left_right_w100h100")
its = 1000
for i in range(its):
    npg.fill_board_with_density(1 / 2)
    negentropy.save_board()
    g.autoupdate(True)
    assert optimize.run_until_converge(
        negentropy, on_run=lambda opt: npg.show(f"{i+1}/{its}", opt)
    )
    g.autoupdate(False)
