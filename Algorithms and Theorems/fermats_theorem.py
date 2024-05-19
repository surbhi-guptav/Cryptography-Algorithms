def power(x, y, p):
    # Calculate x^y % p using binary exponentiation
    result = 1
    x = x % p
    while y > 0:
        # If y is odd, multiply x with result
        if y % 2 == 1:
            result = (result * x) % p
        # y must be even now
        y = y // 2
        x = (x * x) % p
    return result

def is_prime(n, k=5):
    # Perform the Fermat primality test 'k' times
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    for _ in range(k):
        a = 2  # Chosen constant value instead of random number
        # If a^n-1 is not congruent to 1 mod n, then n is composite
        if power(a, n - 1, n) != 1:
            return False
    return True

# Example usage
num = int(input("Enter a number to check if it's prime: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
