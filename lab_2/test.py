import os
import json
import math
import mpmath


pi = {0: 0.2148, 1: 0.3672, 2: 0.2305, 3: 0.1875}


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


def longest_sequence_test(sequence):
    i_seq = list(map(int, sequence))
    block_size = 8
    blocks = [i_seq[i:i + block_size] for i in range(0, len(i_seq), block_size)]
    v = {1: 0, 2: 0, 3: 0, 4: 0}
    for block in blocks:
        max_seq = 0
        temp_max = 0
        for bit in block:
            temp_max = (temp_max + 1) if bit == 1 else 0
            max_seq = max(max_seq, temp_max)
        match max_seq:
            case 0 | 1:
                v[1] += 1
            case 2:
                v[2] += 1
            case 3:
                v[3] += 1
            case 4 | 5 | 6 | 7 | 8:
                v[4] += 1
            case _:
                pass

    x_square = 0
    for i in range(4):
        x_square += math.pow(v[i + 1] - 16 * pi[i], 2) / (16 * pi[i])
    p_value = mpmath.gammainc(3/2, x_square/2)
    
    return p_value


if __name__ == "__main__":
    sequence = "10101010101010001101000000000101101110011101100010010001101001101000011000011110100101011111010111101110010011001011001010111111"
    p_value_frequency = frequency_test(sequence)
    p_value_bits = identical_consecutive_bits(sequence)
    p_value_longest = longest_sequence_test(sequence)
    print("P-value for Frequency Test:", p_value_frequency)
    print("P-value for bits Test:", p_value_bits)
    print("P-value for longest sequence of ones Test:", p_value_longest)