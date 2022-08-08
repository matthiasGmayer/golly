import importlib
import golly as g
import npg
from negentropy import Negentropy

importlib.reload(npg)
from collections import deque


# name = "test"
# width = 100
# height = width
# num_cells = width * height
# num_states = 2**num_cells
# npg.start_board(name=name, height=height, width=width, border="T")
# npg.fill_board_with_density(1 / 2)
# rule = f"b3/s23:P{width},{height}"
# g.setrule(rule)
# g.new(name)
# x0 = -width // 2
# y0 = -height // 2
# whole_board = [x0, y0, width, height]
# xs = range(x0, x0 + width)
# ys = range(y0, y0 + height)
# g.select(whole_board)
# g.fitsel()


# calculate the cumulative states, the number of states with less than 'index' number of live cells
# last = 1
# cum_state_number = [last]
# for k in range(1, height * width + 1):
#     n = height * width
#     last = (n - k + 1) * last // k
#     cum_state_number.append(cum_state_number[-1] + last)


# def fill_board(i):
#     """
#     fill board with the binary representation of 'i'
#     """
#     binary = f"{i:0{num_cells}b}"
#     for i, s in enumerate(binary):
#         if s == "1":
#             g.setcell(i % width - width // 2, i // height - height // 2, 1)
#
#
# def fill_board_randomly():
#     state = random.randint(0, num_states)
#     fill_board(state)
#
#
# def fill_board_with_density(chance=1 / 2):
#     for x in xs:
#         for y in ys:
#             if random.random() < chance:
#                 g.setcell(x, y, 1)


# def negentropy(pop):
#     """
#     Optimization of a state with population "pop"
#     """
#     sums = cum_state_number[pop]
#     # instead of log2( 1 / (x/total) ), log2(total) - log2(x)
#     # bc more numerically stable
#     return num_cells - math.log2(sums)
#
#
# def get_optimization(pop0, pop1):
#     """
#     optimization that ocurred, preference ordering is number of cells alive is good.
#     """
#     return negentropy(pop1) - negentropy(pop0)


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
    negentropy: Negentropy,
    gen_steps=2**5,
    max_steps=2**12,
    mem_size=20,
    criterion=lambda l: is_cycling(l),  # or max_not_increasing(l, 10),
    setup_negentropy=True,
    on_run=lambda opt: None,
):
    """
    gen_steps: how many steps in one iteration
    max_steps: after how many steps abort
    mem_size: how many recent negentropies are kept in memory
    criterion: function that takes the recent negentropies and decides whether the algorithm has converged
    setup_negentropy: if True, negentropy.save_board() is called
    on_run: gets executed after 'gen_steps' generations are run, takes in the optimization of negentropy.
    """
    max_it = max_steps // gen_steps
    last_negentropies = deque()
    if setup_negentropy:
        negentropy.save_board()
    for i in range(max_it):
        g.run(gen_steps)
        opt = negentropy.get_optimization()
        on_run(opt)
        last_negentropies.append(opt)
        if len(last_negentropies) > mem_size:
            last_negentropies.popleft()
            if criterion(last_negentropies):
                return True
    return False


# def run_state_and_get_negentropy():
#     npg.fill_board_with_density()
#     # fill_board_randomly()
#     pop0 = npg.get_pop()
#     run_until_converge()
#     pop1 = npg.get_pop()
#     return get_optimization(pop0, pop1)


# def generate_data(file="random_negentropies.dat", runs=1000):
#     negentropies = []
#     for i in range(runs):
#         g.show(f"{i+1}/{runs}")  # indicate current iteration
#         negentropy = run_state_and_get_negentropy()
#         # negentropies.append(npg.get_pop())
#         negentropies.append(negentropy)
#     os.makedirs("data")
#     with open(f"data/{file}", "w+") as f:
#         f.write("\n".join(map(str, negentropies)))


# generate_data(file="ending_populations.dat", runs=1000)
# generate_data(runs=1000)
# print([(i, omega(i)) for i in range(1000) if 7900 <= omega(i) <= 8100])

# fill_board_randomly()
# g.fit()

# display progress
# g.autoupdate(True)
# steps = run_until_converge()
# board = g.getcells(whole_board)
# g.show(str(steps))
# pop0 = int(g.getpop())
# g.run(2**10)
# pop1 = int(g.getpop())
# negentropy = get_negentropy(pop0, pop1)
# g.show(str(negentropy))

# fill_board_with_density(0.5)
