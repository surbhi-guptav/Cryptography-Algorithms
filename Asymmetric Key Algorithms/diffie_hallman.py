import random

# Function to perform Diffie-Hellman key exchange
def diffie_hellman():
    # Publicly agreed prime number and base (primitive root)
    p = int(input("Enter the prime number P : ")) # Example prime number
    g = int(input("Enter the primitive root : "))  # Example primitive root

    # Alice's private key
    a = random.randint(1, p - 1)
    # Bob's private key
    b = random.randint(1, p - 1)

    # Calculate public keys
    A = (g ** a) % p
    B = (g ** b) % p

    # Shared secret calculation
    shared_secret_Alice = (B ** a) % p
    shared_secret_Bob = (A ** b) % p

    # Both parties now have the same shared secret
    return shared_secret_Alice, shared_secret_Bob

# Perform Diffie-Hellman key exchange
Alice_shared_secret, Bob_shared_secret = diffie_hellman()

# Print shared secrets
print("Alice's shared secret:", Alice_shared_secret)
print("Bob's shared secret:", Bob_shared_secret)
