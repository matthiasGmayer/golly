import golly as g
import random
import math
import logging
import os
from collections import deque

logging_file = "log_optimize.log"
os.system(f"> {logging_file}")  # wipe logging file
logging.basicConfig(filename=logging_file)
logging.getLogger().setLevel(logging.INFO)


name = "test"
width = 100
height = width
num_cells = width * height
num_states = 2**num_cells
rule = f"b3/s23:P{width},{height}"
g.setrule(rule)
g.new(name)
x0 = -width // 2
y0 = -height // 2
g.select([x0, y0, width, height])

# calculate the cumulative states, the number of states with less than 'index' number of live cells
last = 1
cum_state_number = [last]
for k in range(1, height * width + 1):
    n = height * width
    last = (n - k + 1) * last // k
    cum_state_number.append(cum_state_number[-1] + last)


def fill_board(i):
    """
    fill board with the binary representation of 'i'
    """
    binary = f"{i:0{num_cells}b}"
    for i, s in enumerate(binary):
        if s == "1":
            g.setcell(i % width - width // 2, i // height - height // 2, 1)


def fill_board_randomly():
    state = random.randint(0, num_states)
    fill_board(state)


def omega(pop):
    """
    Optimization of a state with population "pop"
    """
    sums = cum_state_number[pop]
    # instead of log2( 1 / (x/total) ), log2(total) - log2(x)
    # bc more numerically stable
    return num_cells - math.log2(sums)


def get_pop():
    return int(g.getpop())


def get_negentropy(pop0, pop1):
    """
    optimization that ocurred, preference ordering is number of cells alive is good.
    """
    return omega(pop1) - omega(pop0)


def cauchy(list, tol):
    return max(list) - min(list) < tol


def max_not_increasing(list, interval):
    maxs = [max(list[i : -interval + i]) for i in range(interval)]
    return all(m == maxs[0] for m in maxs)


def is_cycling(neg_list, times=3):
    neg_list = list(reversed(neg_list))
    for period in range(1, len(neg_list) // times):
        slices = [neg_list[period * i : period * (i + 1)] for i in range(times)]
        if all(s == slices[0] for s in slices):
            return True


def run_until_converge(
    gen_steps=2**5,
    max_it=2**15,
    mem_size=20,
    criterion=lambda l: is_cycling(l),  # or max_not_increasing(l, 10),
):
    max_it = max_it // gen_steps
    initial_population = get_pop()
    # biggest_negentropy = omega(initial_population)
    last_negentropies = deque()
    for i in range(max_it):
        g.run(gen_steps)
        population = get_pop()
        negentropy = get_negentropy(initial_population, population)
        last_negentropies.append(negentropy)
        if len(last_negentropies) > mem_size:
            last_negentropies.popleft()
            if criterion(last_negentropies):
                break
    return i * gen_steps


def run_state_and_get_negentropy():
    fill_board_randomly()
    pop0 = get_pop()
    run_until_converge()
    pop1 = get_pop()
    return get_negentropy(pop0, pop1)


def generate_data(file="random_negentropies.dat", runs=1000):
    negentropies = []
    for i in range(runs):
        g.show(f"{i+1}/{runs}")  # indicate current iteration
        negentropy = run_state_and_get_negentropy()
        # negentropies.append(get_pop())
        negentropies.append(negentropy)
    os.makedirs("data")
    with open(f"data/{file}", "w+") as f:
        f.write("\n".join(map(str, negentropies)))


# generate_data(file="ending_populations.dat", runs=1000)
generate_data(runs=1000)

# print([(i, omega(i)) for i in range(1000) if 7900 <= omega(i) <= 8100])

# fill_board_randomly()
# g.fit()

# display progress
# g.autoupdate(True)
# steps = run_until_converge()

# g.show(str(steps))
# pop0 = int(g.getpop())
# g.run(2**10)
# pop1 = int(g.getpop())
# negentropy = get_negentropy(pop0, pop1)
# g.show(str(negentropy))
