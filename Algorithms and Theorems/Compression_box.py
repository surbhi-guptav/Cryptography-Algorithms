def compressed_six_to_four(bits):
    # Ensure input is 6 bits
    if len(bits) != 6:
        raise ValueError("Input must be 6 bits long")

    # Define compression mapping using XOR and OR operators
    compressed_bits = ''
    compressed_bits += bits[0] + bits[1]
    compressed_bits += '0' if bits[1] == '1' else '1'  # XOR operation
    compressed_bits += '0' if bits[3] == '1' else '1'  # XOR operation

    return compressed_bits

# Example usage
input_bits = '101001'
compressed_bits = compressed_six_to_four(input_bits)
print("Compressed Bits:", compressed_bits)