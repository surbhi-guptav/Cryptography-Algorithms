def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

# Example usage:
a = 67
b = 72
gcd, x, y = extended_gcd(a, b)

print(f"GCD({a}, {b}) = {gcd}")
print(f"x = {x}, y = {y}")
print(f"{x}*{a} + {y}*{b} = {gcd}")
