# Define the irreducible polynomial in binary representation for GF(2^8)
IRREDUCIBLE_POLY = 0b100011011  # x^8 + x^4 + x^3 + x + 1

# Function to multiply two numbers in GF(2^8)
def gf_multiply(a, b):
    result = 0
    for _ in range(8):
        if b & 1:  # If the least significant bit of b is 1
            result ^= a  # Add a to the result
        high_bit_set = a & 0x80  # Check if the highest bit of a is 1
        a <<= 1  # Left shift a by 1
        if high_bit_set:  # If the highest bit of a was 1
            a ^= IRREDUCIBLE_POLY  # Reduce a by XOR with the irreducible polynomial
        b >>= 1  # Right shift b by 1
    return result

# Function to perform finite field addition
def gf_add(a, b):
    return a ^ b

# Function to perform finite field subtraction (subtraction is the same as addition in GF(2^8))
def gf_subtract(a, b):
    return gf_add(a, b)

# Function to perform finite field division
def gf_divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is undefined in finite field")
    # Division in GF(2^8) is the same as multiplication with the multiplicative inverse
    # Multiplicative inverse of b is b^(2^8 - 2) (as GF(2^8) is a field of characteristic 2)
    inverse_b = pow(b, 0xFF, 0x1FF)  # 0xFF is 2^8 - 2
    return gf_multiply(a, inverse_b)

# Example usage
a = 0b11011011  # 219 in decimal
b = 0b10010101  # 149 in decimal

# Multiply a and b in GF(2^8)
product = gf_multiply(a, b)
print("Product (a * b) in GF(2^8):", bin(product))

# Add a and b in GF(2^8)
summation = gf_add(a, b)
print("Sum (a + b) in GF(2^8):", bin(summation))

# Subtract b from a in GF(2^8)
difference = gf_subtract(a, b)
print("Difference (a - b) in GF(2^8):", bin(difference))

# Divide a by b in GF(2^8)
quotient = gf_divide(a, b)
print("Quotient (a / b) in GF(2^8):", bin(quotient))
