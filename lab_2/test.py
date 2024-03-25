import os
import json
import math


def frequency_test(sequence):
    n = len(sequence)
    ones_count = sequence.count('1')
    zeroes_count = sequence.count('0')
    s_obs = abs(ones_count - zeroes_count) / math.sqrt(n)
    p_value = math.erfc(s_obs / math.sqrt(2))
    return p_value


