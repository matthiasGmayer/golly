from matplotlib import pyplot as plt

data_file = "data/random_negentropies.dat"
with open(data_file) as file:
    lines = file.read().strip().split("\n")
    negentropies = list(map(float, lines))


def histogram():
    plt.hist(negentropies)
    plt.savefig("plots/random_negentropies.png")
    plt.show()


def density():
    x = sorted(negentropies)
    y = [1 / sum(abs(n - n2) for n2 in x) for n in x]
    plt.plot(x, y)
    plt.savefig("plots/random_negentropies_1_over_sum.png")
    plt.show()


density()
