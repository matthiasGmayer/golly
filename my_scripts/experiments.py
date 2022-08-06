import importlib
import npg

importlib.reload(npg)
import negentropy

importlib.reload(negentropy)
from negentropy import *
import optimize

importlib.reload(optimize)
from optimize import run_until_converge

import golly as g


def save_best_worst(n, name, negentropy: Negentropy, mem_size=10, load=True):
    i = 0
    min_opt = max_opt = None, None
    if load:
        best_opts = np.load(f"data/{name}_best_opts.npy")
        worst_opts = np.load(f"data/{name}_worst_opts.npy")
        best_boards = np.load(f"data/{name}_best_boards.npy")
        worst_boards = np.load(f"data/{name}_worst_boards.npy")
    else:
        best_opts = np.array([])
        worst_opts = np.array([])
        best_boards = None
        worst_boards = None
    while True:
        i = i + 1
        npg.fill_board_with_density(1 / 2)
        negentropy.save_board()
        run_until_converge()
        opt = negentropy.get_optimization()
        if len(best_opts) < mem_size:
            best_opts = np.append(best_opts, opt)
            if best_boards is None:
                best_boards = np.array([negentropy.saved_board])
            else:
                best_boards = np.append(best_boards, [negentropy.saved_board], axis=0)
        else:
            index, min_opt = min(enumerate(best_opts), key=lambda x: x[1])
            if min_opt < opt:
                best_opts[index] = opt
                best_boards[index] = negentropy.saved_board
        if len(worst_opts) < mem_size:
            worst_opts = np.append(best_opts, opt)
            if worst_boards is None:
                worst_boards = np.array([negentropy.saved_board])
            else:
                worst_boards = np.append(best_boards, [negentropy.saved_board], axis=0)
        else:
            index, max_opt = max(enumerate(worst_opts), key=lambda x: x[1])
            if max_opt > opt:
                worst_opts[index] = opt
                worst_boards[index] = negentropy.saved_board
        if i % 100 == 0:
            np.save(f"data/{name}_best_opts", best_opts)
            np.save(f"data/{name}_worst_opts", worst_opts)
            np.save(f"data/{name}_worst_boards", worst_boards)
            np.save(f"data/{name}_best_boards", best_boards)
            break
        npg.show(i, min_opt, max_opt)


width, height = 100, 100
npg.start_board(
    width=width,
    height=height,
)

# --
negentropy = NumberOfCells([0, 0, 0, 0], [0, 0, width, height])
save_best_worst(0, "num_cells/best_worst", negentropy, load=False)
# --

# --
# negentropy = NumberOfCells([0, 0, width//2, height], [width//2+1, 0, width//2, height])
# save_best_worst(0, "/best_worst", negentropy)
# --
