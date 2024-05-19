def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    else:
        return x % m

# Example usage:
a = int(input("Enter the value of a : "))
m = int(input("Enter the value of m : "))

inverse = mod_inverse(a, m)
print(f"The modular multiplicative inverse of {a} under {m} is {inverse}")
