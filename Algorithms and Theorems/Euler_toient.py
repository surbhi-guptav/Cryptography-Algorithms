def euler_totient(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    phi = n  # Initialize phi to n, and we will subtract for each non-coprime number
    p = 2  # Start with the smallest prime number

    while p * p <= n:
        if n % p == 0:  # p is a prime factor of n
            while n % p == 0:
                n //= p
            phi -= phi // p

        p += 1

    if n > 1:
        phi -= phi // n

    return phi

# Example usage:
n = int (input("Enter the value : "))
result = euler_totient(n)
print(f"Euler Totient function φ({n}) = {result}")
