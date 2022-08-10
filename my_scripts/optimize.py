import importlib
import golly as g
import npg
from negentropy import Negentropy

importlib.reload(npg)
from collections import deque


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
    mem_size=50,
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
