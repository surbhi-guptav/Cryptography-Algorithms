def expand_four_to_six(bits):
    # Ensure input is 4 bits
    if len(bits) != 4:
        raise ValueError("Input must be 4 bits long")

    # Define expansion mapping using XOR and OR operators
    expanded_bits = ''
    expanded_bits += bits[0] + bits[1]
    expanded_bits += '0' if bits[1] == '1' else '1'  # XOR operation
    expanded_bits += bits[2]
    expanded_bits += bits[2]  # Repeat the bit
    expanded_bits += '0' if bits[3] == '1' else '1'  # XOR operation

    return expanded_bits

# Example usage
input_bits = '1010'
expanded_bits = expand_four_to_six(input_bits)
print("Expanded Bits:", expanded_bits)
