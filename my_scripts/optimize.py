import golly as g
import random
import math


cum_state_number = []


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

    # calculate the cumulative states, the number of states with less than 'index' number of live cells
    last = 1
    cum_state_number.append(last)
    for k in range(1, height * width + 1):
        n = height * width
        last = (n - k + 1) * last // k
        cum_state_number.append(cum_state_number[-1] + last)


initialize()


def fill_board(i):
    """
    fill board with the binary representation of 'i'
    """
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


def omega(pop):
    """
    Optimization of a state with population "pop"
    """
    height = g.getheight()
    width = g.getwidth()
    num_cells = width * height
    sums = cum_state_number[pop]
    # instead of log2( 1 / (x/total) ), log2(total) - log2(x)
    # bc more numerically stable
    return num_cells - math.log2(sums)


def get_negentropy(pop0, pop1):
    """
    optimization that ocurred, preference ordering is number of cells alive is good.
    """
    return omega(pop1) - omega(pop0)


fill_board_randomly()
pop0 = int(g.getpop())
g.run(2**10)
pop1 = int(g.getpop())
negentropy = get_negentropy(pop0, pop1)
g.show(str(negentropy))

g.fit()
