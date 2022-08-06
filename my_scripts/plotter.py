from matplotlib import pyplot as plt
from scipy import interpolate, optimize
import numpy as np
import os

data = "random_negentropies"
# data = "ending_populations"
data_file = f"data/{data}.dat"
# os.makedirs("plots")
with open(data_file) as file:
    lines = file.read().strip().split("\n")
    negentropies = list(map(float, lines))


def histogram():
    plt.hist(negentropies)
    plt.savefig(f"plots/{data}.png")
    plt.show()


def inverse_sum():
    x = sorted(negentropies)
    y = [1 / sum(abs(n - n2) for n2 in x) for n in x]
    plt.plot(x, y)
    plt.savefig(f"plots/{data}_1_over_sum.png")
    plt.show()


def get_cdf():
    x = sorted(negentropies)
    y = [(i + 1) / (len(x) + 1) for i in range(len(x))]
    xy = list(zip(x, y))
    xy = [(x, y) for (x, y), (x1, y1) in zip(xy, xy[1:] + [(None, None)]) if x != x1]
    x, y = zip(*xy)
    x = np.array(x)
    y = np.array(y)
    return x, y


def smooth_cdf(n=10):
    x, y = get_cdf()
    nl = len(x) // n
    x, y = x[: nl * n], y[: nl * n]
    x = np.reshape(x, (nl, n))
    y = np.reshape(y, (nl, n))
    x = np.average(x, axis=1)
    y = np.average(y, axis=1)

    return x, y


def interpolation_pdf():
    # x, y = smooth_cdf(n=20)
    x, y = get_cdf()
    ydiff = y[1:] - y[:-1]
    xdiff = x[1:] - x[:-1]
    diff = ydiff / xdiff
    avgdiff_stack = np.stack([diff[1:], diff[:-1]])
    avgdiff = np.average(avgdiff_stack, axis=0)
    slope = np.concatenate(([diff[0]], avgdiff, [diff[-1]]))
    plt.plot(x, slope)
    plt.show()


interpolation_pdf()
# histogram()
