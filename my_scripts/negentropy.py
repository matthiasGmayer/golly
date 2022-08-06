import numpy as np
import math
import copy
import npg
import zlib
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
        raise NotImplemented

    def __getitem__(self, board):
        num_states = self.get_number_states(board)
        return self.num_cells - math.log2(num_states)


# All have uniform distribution
class Kolmogorov(Negentropy):
    def board_to_bytes(self, board):
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
        bin = self.board_to_bytes(board)
        compressed = zlib.compress(bin)
        return len(compressed) - self.baseline

    def __init__(self, width, height) -> None:
        super().__init__()
        board = npg.get_board_from_int(0, width, height)
        bin = self.board_to_bytes(board)
        compressed = zlib.compress(bin)
        self.baseline = len(compressed)

    def get_number_states(self, board):
        pass


class NumberOfCells(Negentropy):
    def get_distribution(self, n):
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
            for ni, n in enumerate(neg_distr):
                d[pi - ni] += p * n
        cum = defaultdict(int)
        maxkey = max(d.keys())
        minkey = min(d.keys())
        # cum[minkey] = d[minkey]
        # for i in range(minkey + 1, maxkey + 1):
        #     cum[i] = cum[i - 1] + d[i]
        cum[maxkey] = d[maxkey]
        for i in range(maxkey - 1, minkey - 1, -1):
            cum[i] = cum[i + 1] + d[i]
        self.util_to_num_states = cum

    def get_number_states(self, board):
        """
        return negentropy of specified board
        """

        def get_sub_board(b, x, y, w, h):
            return b[x : x + w, y : y + h]

        pos_area = get_sub_board(board, *self.positive_rect)
        neg_area = get_sub_board(board, *self.negative_rect)
        util = np.sum(pos_area) - np.sum(neg_area)
        return self.util_to_num_states[util]
