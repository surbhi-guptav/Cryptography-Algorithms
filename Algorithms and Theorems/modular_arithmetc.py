def mod_add(a, b, modulus):
    # Modular addition: (a + b) % modulus
    return (a + b) % modulus

def mod_subtract(a, b, modulus):
    # Modular subtraction: (a - b) % modulus
    return (a - b) % modulus

def mod_multiply(a, b, modulus):
    # Modular multiplication: (a * b) % modulus
    return (a * b) % modulus

def mod_inverse(a, modulus):
    # Modular multiplicative inverse: a^-1 % modulus
    for x in range(1, modulus):
        if (a * x) % modulus == 1:
            return x
    return None  # No modular inverse exists

def mod_exponentiation(base, exp, modulus):
    # Modular exponentiation: (base^exp) % modulus
    result = 1
    base = base % modulus
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % modulus
        exp //= 2
        base = (base * base) % modulus
    return result

# Example usage:
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
modulus = 7

result_add = mod_add(a, b, modulus)
result_subtract = mod_subtract(a, b, modulus)
result_multiply = mod_multiply(a, b, modulus)
result_inverse = mod_inverse(a, modulus)
result_exponentiation = mod_exponentiation(a, b, modulus)

print("Modular Addition:", result_add)
print("Modular Subtraction:", result_subtract)
print("Modular Multiplication:", result_multiply)
print("Modular Inverse:", result_inverse)
print("Modular Exponentiation:", result_exponentiation)
