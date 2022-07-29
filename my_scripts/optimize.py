import golly as g
from glife import *
import random
import math


sums_omega = []


def initialize():
    name = "test"
    width = 100
    height = width
    rule = f"b3/s23:P{width},{height}"
    g.setrule(rule)
    g.new(name)
    x0 = -width // 2
    y0 = -height // 2
    g.select([x0, y0, width, height])
    last = 1
    sums_omega.append(last)
    for k in range(1, height * width):
        n = height * width
        last = (n - k + 1) * last // k
        sums_omega.append(sums_omega[-1] + last)


initialize()


def fill_board(i):
    height = g.getheight()
    width = g.getwidth()
    num_cells = width * height
    binary = f"{i:0{num_cells}b}"
    for i, s in enumerate(binary):
        if s == "1":
            g.setcell(i % width - width // 2, i // height - height // 2, 1)


def fill_board_randomly():
    height = g.getheight()
    width = g.getwidth()
    num_cells = width * height
    states = 2**num_cells
    state = random.randint(0, states)
    fill_board(state)


log2states = math.log2(sums_omega[-1])


def omega(pop):
    sums = sums_omega[pop]
    return log2states - math.log2(sums)


def get_optimization(pop0, pop1):
    """
    optimization that ocurred, preference ordering is number of cells alive is good.
    """
    return omega(pop1) - omega(pop0)


fill_board_randomly()
# g.show(str(g.getcells([0, 0, 10, 10])))
g.show(str(g.getxy()))


# pop0 = int(g.getpop())

# g.run(2**10)

# pop1 = int(g.getpop())
# optimization = get_optimization(pop0, pop1)

# g.show(str(optimization))

# g.fit()

# for i in range(10):
#     g.randfill(50)
#     g.run(2**15)
