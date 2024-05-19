import random

def generate_homophonic_key(alphabet):
    key = {}
    for char in alphabet:
        num_substitutions = random.randint(1, 5)  # Randomly choose how many substitutions for each character
        substitutions = ''.join(random.choice(alphabet) for _ in range(num_substitutions))
        key[char] = substitutions
    return key

def encrypt_homophonic(message, key):
    encrypted_message = ""
    for char in message.upper():  # Convert to uppercase for simplicity
        if char in key:
            substitutions = key[char]
            encrypted_char = random.choice(substitutions)  # Choose a random substitution
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

# Example usage
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
message = "thisisHomophonicCipherImplementation"
homophonic_key = generate_homophonic_key(alphabet)
encrypted_message = encrypt_homophonic(message, homophonic_key)

print("Original message:", message)
print("Encrypted message:", encrypted_message)
