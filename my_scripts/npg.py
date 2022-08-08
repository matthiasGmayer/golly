import golly as g
import numpy as np
import logging
import os

logging_file = "log.log"
os.system(f"> {logging_file}")  # wipe logging file
logging.basicConfig(filename=logging_file)
logging.getLogger().setLevel(logging.INFO)


def get_step():
    return g.getstep()


def show(*to_show, sep=" "):
    g.show(sep.join(str(s) for s in to_show))


def log(string):
    logging.info(string)
    print(string)
    show(string)


def set_logging_file(file):
    if not file.endswith(".log"):
        file += ".log"
    global logging_file
    logging_file = file


def set_cell(x: int, y: int, state: int):
    """
    0 <= x,y <= dimensions
    """
    g.setcell(x - get_width() // 2, y - get_height() // 2, int(state))


def set_cells(xs, ys, states):
    for x, y, state in zip(xs, ys, states):
        set_cell(x, y, state)


def set_rect(array, x0=0, y0=0):
    n, m = array.shape
    for x in range(n):
        for y in range(m):
            set_cell(x0 + x, y0 + y, array[x, y])


def get_rect(x0, y0, width, height):
    """
    return the specified rect as numpy array with 0's and 1's
    """
    bin = np.zeros((width, height))
    cells = g.getcells([x0 - get_width() // 2, y0 - get_height() // 2, width, height])
    cells = np.array(cells)
    cells = np.reshape(cells, (-1, 2))
    bin[cells[:, 0] + get_width() // 2, cells[:, 1] + get_height() // 2] = 1
    return bin


def set_board(array):
    assert array.shape == (get_width(), get_height())
    set_rect(array)


def get_board():
    return get_rect(0, 0, get_width(), get_height())


def get_pop():
    return int(g.getpop())


def get_width():
    return g.getwidth()


def get_height():
    return g.getheight()


def get_shape():
    return get_width(), get_height()


def select(rect):
    ox = get_width() // 2
    oy = get_height() // 2
    g.select([rect[0] - ox, rect[1] - oy, rect[2], rect[3]])


def fill_board_with_density(density=1 / 2):
    set_board(np.random.random(get_shape()) > density)


def get_board_from_int(n, width, height):
    l = []
    for b in f"{n:0{width*height}b}":
        l.append(int(b))
    return np.array(l).reshape((width, height))


def get_all_boards(width, height):
    for i in range(2 ** (width * height)):
        yield (get_board_from_int(i, width, height))


# rule = f"b3/s23:P{width},{height}"
def start_board(name="optimization", width="", height="", rule="b3/s23", border="P"):
    if rule != "" and width != "" != height:
        rule = f"{rule}:{border}{width},{height}"
    g.setrule(rule)
    g.new(name)
    if width != "" != height:
        select([0, 0, width, height])
        g.fitsel()
