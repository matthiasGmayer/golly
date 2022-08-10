import numpy as np
import math
import copy
import pickle
import npg
import zlib
import compression
from collections import defaultdict


class Negentropy:
    def __init__(self) -> None:
        w, h = npg.get_width(), npg.get_height()
        self.num_cells = w * h
        self.saved_board = np.zeros((w, h))

    def get_optimization(self, board0=None, board1=None):
        """
        board0, board1 are arguments for the negentropy
        optimization that ocurred between
        If board0 is None, it gets set to the board saved by save_board()
        If board1 is None, it gets set to the current board
        """
        if board0 is None:
            board0 = self.saved_board
        if board1 is None:
            board1 = npg.get_board()
        return self[board1] - self[board0]

    def save_board(self, board=None):
        """
        save a board that can be used for get_optimization()
        if 'board' is None: save the current board
        """
        if board is None:
            board = npg.get_board()
        self.saved_board = copy.deepcopy(board)

    def get_number_states(self, board):
        """to implement in subclass"""
        pass

    def __getitem__(self, board):
        """
        Calculates the negentropy of a board
        """
        num_states = self.get_number_states(board)
        return self.num_cells - math.log2(num_states)

    def save(self, name):
        """
        save this negentropy object to data/negentropies/{name}
        """
        fname = f"data/negentropies/{name}"
        with open(fname, "wb+") as file:
            pickle.dump(self, file)


def load(name):
    """
    load a negentropy from data/negentropies/{name}
    """
    fname = f"data/negentropies/{name}"
    with open(fname, "rb") as file:
        obj = pickle.load(file)
    return obj


class Kolmogorov(Negentropy):
    """
    Define a negentropy by using the Kolmogorov complexity as a loss function.
    The Kolmogorov complexity is approximated by a compression algorithm (compression.py)
    """

    def board_to_bytes(self, board):
        """
        function to convert the board to bytes to use gzip on.
        """
        # board = board.reshape(-1)
        # board = np.concatenate((board, np.zeros((-len(board) % 8), dtype="int32")))
        # board = board.reshape((-1, 8))
        # board *= np.array([int(2**i) for i in range(8)])
        # board = np.sum(board, axis=1).tolist()
        # bytes = b"".join(i.to_bytes(1, byteorder="little") for i in board)
        # return bytes
        board = board.reshape(-1).tolist()
        bytes = b"".join(i.to_bytes(1, byteorder="little") for i in board)
        return bytes

    def compression_length(self, board):
        """
        returns the compression length of the board with compression.py
        """
        # bin = self.board_to_bytes(board)
        # compressed = zlib.compress(bin)
        # return len(compressed)
        compressed = compression.compress(board.reshape((-1)))
        return len(compressed)

    def __init__(self) -> None:
        super().__init__()

    def get_number_states(self, board):
        """
        estimate the number of boards with less compression length by assuming every bit is mapped
        """
        c = self.compression_length(board)
        return 2 ** (c + 1) - 1


class NumberOfCells(Negentropy):
    """
    Define a negentropy by using a utility function.
    Every alive cell in the positive area gives 1 utility.
    Every alive cell in the negative are gives -1 utility.
    """

    def get_distribution(self, n):
        """
        returns [n choose k for k in range(n+1)]
        """
        last = 1
        cum = [last]
        for k in range(1, n + 1):
            last = (n - k + 1) * last // k
            cum.append(last)
        return cum

    def __init__(self, positive_rect, negative_rect):
        """
        rect = [x0,y0,width,height]
        utility(state) = sum(positive_area) - sum(negative_area) where area is the np_array with 1's for alive
        This takes a long time to initalize!
        Consider saving and loading the negentropy.
        """
        super().__init__()
        self.positive_rect = positive_rect
        self.negative_rect = negative_rect
        pos_size = positive_rect[2] * positive_rect[3]
        neg_size = negative_rect[2] * negative_rect[3]
        pos_distr = self.get_distribution(pos_size)
        neg_distr = self.get_distribution(neg_size)

        d = defaultdict(int)
        for pi, p in enumerate(pos_distr):
            npg.log(f"{pi}/{len(pos_distr)}")
            for ni, n in enumerate(neg_distr):
                d[pi - ni] += p * n
        cum = defaultdict(int)
        maxkey = max(d.keys())
        minkey = min(d.keys())
        cum[minkey] = d[minkey]
        for i in range(minkey + 1, maxkey + 1):
            cum[i] = cum[i - 1] + d[i]
        cum[maxkey] = d[maxkey]
        for i in range(maxkey - 1, minkey - 1, -1):
            cum[i] = cum[i + 1] + d[i]
        self.util_to_num_states = cum

    def get_util(self, board):
        """
        return the utility of the board
        """

        def get_sub_board(b, x, y, w, h):
            return b[x : x + w, y : y + h]

        pos_area = get_sub_board(board, *self.positive_rect)
        neg_area = get_sub_board(board, *self.negative_rect)
        util = np.sum(pos_area) - np.sum(neg_area)
        return util

    def get_number_states(self, board):
        """
        return negentropy of specified board
        """
        util = self.get_util(board)
        return self.util_to_num_states[util]
