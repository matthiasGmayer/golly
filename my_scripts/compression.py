import math


def binary_to_val(bin_list):
    """
    converts binary to numerical
    Example: [1,0,1] -> 5
    """
    if not bin_list:
        return 0
    return int("".join(map(str, bin_list)), base=2)


def val_to_binary(val):
    """
    converts value to binary
    Example: 5 -> [1,0,1]
    """
    return list(map(int, f"{val:b}"))


def binary_l(n, l):
    """
    gives the binary end of the encoding of number n, if there are l 1's in the encoding beginning
    """
    v = n - 2**l + 1
    return list(map(int, f"{v:0{l}b}"))[:l]


def encode(n):
    """
    encodes a length into binary
    there is a prefix of m 1's followed by a 0
    the number of 1's is the length of the binary number that follows.
    Examples:
    0 : 0
    1 : 10 0
    2 : 10 1
    3 : 110 00
    4 : 110 01
    5 : 110 10 etc.
    """
    l = math.floor(math.log2(n + 1))
    return [1] * l + [0] + binary_l(n, l)


def decode(stream):
    """
    split the stream into units and decode them.
    Example:
    00010111000 -> 0 0 0 101 11000
    see 'encode' for further clarification
    """
    if not stream:
        return []
    idx = stream.index(0)
    val_bits = stream[idx + 1 : 2 * idx + 1]
    val = binary_to_val(val_bits)
    num_under = 2**idx - 1
    return [val + num_under] + decode(stream[(2 * idx + 1) :])


def to_list(gen):
    def wrapper(*args, **kwargs):
        return list(gen(*args, **kwargs))

    return wrapper


@to_list
def compress(bits):
    """
    yield the starting bit (0 or 1) and after that
    and encoded version of (length-1) of the alternating patterns:
    Example:
    1110100
    starts with 1 -> 1
    encoded(2) -> 101
    encoded(0) -> 0
    encoded(0) -> 0
    encoded(1) -> 100
    Result: 110100100

    The compression only works well when the streaks are long
    """
    yield bits[0]
    length = 0
    for b0, b1 in zip(bits[:-1], bits[1:]):
        if b0 != b1:
            yield from encode(length)
            length = 0
        else:
            length += 1
    yield from encode(length)


def decompress(bits):
    s = bits[0]
    lengths = decode(bits[1:])
    l = []
    for length in lengths:
        l += [s] * (length + 1)
        s = 1 - s
    return l
