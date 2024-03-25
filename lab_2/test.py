import os
import json
import math


def frequency_test(sequence):
    ones_count = sequence.count('1')
    zeros_count = sequence.count('0')
    s_obs = abs(ones_count - zeros_count)
    p_value = math.erfc(s_obs / math.sqrt(len(sequence)) / math.sqrt(2))
    return p_value


if __name__ == "__main__":
    sequence = "10101010101010001101000000000101101110011101100010010001101001101000011000011110100101011111010111101110010011001011001010111111"
    p_value_frequency = frequency_test(sequence)
    print("P-value for Frequency Test:", p_value_frequency)