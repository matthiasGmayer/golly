# import negentropy.NumberOfCells
from negentropy import NumberOfCells, Kolmogorov
import math
import numpy as np
import npg
from matplotlib import pyplot as plt


def test_number_of_cells():
    n, m = 3, 3
    board_shape = n, m
    positive = [1, 0, 1, 3]
    negative = [0, 0, 1, 3]
    negentropy = NumberOfCells(positive, negative)
    for x in range(n * m + 1):
        a = np.array([0] * x + [1] * (n * m - x))
        a = np.reshape(a, (n, m))
        # print(a)
        # print(negentropy[a])
        # this is correct


def test_kolmogorov():
    # n, m = 100, 100
    n, m = 24, 24
    board_shape = n, m
    negentropy = Kolmogorov()
    # for x in range(n * m + 1):
    #     a = np.array([0] * x + [1] * (n * m - x))
    #     a = np.reshape(a, (n, m))
    #     print(negentropy[a])

    # board = np.array([0, 1] * 5000).reshape(board_shape)
    # negentropy[board]
    for x in range(100000):
        board = np.random.random(board_shape) > 5 / 6
        # print(board)
        negentropy[board]


def plot_all_kolmogorov(width, height):
    npg.start_board(width=width, height=height)
    negentropy = Kolmogorov(width, height)
    boards = [
        print(f"{i+1}/{2**(width*height)}") or b
        for i, b in enumerate((npg.get_all_boards(width, height)))
    ]
    compressed_lengths = []
    for b in boards:
        npg.set_board(b)
        compressed_lengths.append(negentropy.compression_length(b.reshape(-1)))
        for i in range(1000):
            npg.step()
            compressed_lengths.append(
                negentropy.compression_length(npg.get_board().reshape(-1))
            )

    plt.hist(compressed_lengths)
    # x = range(max(compressed_lengths))
    # y = [2**i for i in x]
    # plt.plot(x, y)
    plt.show()


def test_pos_neg_negentropy():
    w, h = 100, 100
    w2, h2 = w // 2, h // 2
    negentropy = NumberOfCells([0, 0, w2, h], [w2, 0, w2, h])


plot_all_kolmogorov(4, 4)
# test_kolmogorov()
# test_pos_neg_negentropy()
