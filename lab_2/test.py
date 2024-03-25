import os
import json
from math import erfc


def frequency_test(bitstring):
    n = len(bitstring)
    ones = bitstring.count('1')
    proportion = abs(ones / n - 0.5)
    s_obs = 2 * proportion / (n ** 0.5)
    p_value = erfc(s_obs / 2 ** 0.5)

    return p_value
