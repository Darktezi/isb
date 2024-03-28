import os
import json
import math


def frequency_test(sequence):
    ones_count = sequence.count('1')
    zeros_count = sequence.count('0')
    s_obs = math.fabs(ones_count - zeros_count)
    p_value = math.erfc(s_obs / math.sqrt(len(sequence)) / math.sqrt(2))
    return p_value


def identical_consecutive_bits(sequence):
    proportion = sequence.count('1') / len(sequence)
    if math.fabs(proportion - 0.5) > (2/math.sqrt(len(sequence))):
                return 0
    v = 0
    for i in range(0, len(sequence) - 1):
          v += 1 if sequence[i] != sequence[i +  1] else 0
    p_value = math.erfc(math.fabs(v-2*len(sequence)*proportion*(1-proportion))/(2*math.sqrt(2*len(sequence))*proportion*(1-proportion)))
    return p_value


if __name__ == "__main__":
    sequence = "10101010101010001101000000000101101110011101100010010001101001101000011000011110100101011111010111101110010011001011001010111111"
    p_value_frequency = frequency_test(sequence)
    p_value_bits = identical_consecutive_bits(sequence)
    print("P-value for Frequency Test:", p_value_frequency)
    print("P-value for bits Test:", p_value_bits)