import random

# Convert text to bits
def text_to_bits(text):
    bits = []
    for char in text:
        binary_representation = bin(ord(char))[2:].zfill(8)  # Convert character to 8-bit binary
        bits.extend([int(bit) for bit in binary_representation])
    return bits

# Convert bits to text
def bits_to_text(bits):
    binary_string = ''.join(str(bit) for bit in bits)
    text = ""
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        text += chr(int(byte, 2))
    return text

# Key Generation: Generate a random key of a specific length
def generate_key(key_length):
    key = []
    for _ in range(key_length):
        key.append(random.randint(0, 1))  # Key bits are either 0 or 1
    return key

# Encryption: XOR the plaintext bits with the key bits to get the ciphertext bits
def encrypt(plaintext_bits, key):
    ciphertext_bits = []
    for i in range(len(plaintext_bits)):
        # Perform XOR operation between plaintext bit and key bit at the same position
        ciphertext_bit = plaintext_bits[i] ^ key[i % len(key)]
        ciphertext_bits.append(ciphertext_bit)
    return ciphertext_bits

# Decryption: XOR the ciphertext bits with the key bits to get the plaintext bits back
def decrypt(ciphertext_bits, key):
    plaintext_bits = []
    for i in range(len(ciphertext_bits)):
        # Perform XOR operation between ciphertext bit and key bit at the same position
        plaintext_bit = ciphertext_bits[i] ^ key[i % len(key)]
        plaintext_bits.append(plaintext_bit)
    return plaintext_bits

# Example usage
plaintext_text = "thisisstreamcipherimplementation"  # Example input text
plaintext_bits = text_to_bits(plaintext_text)  # Convert text to bits

key_length = len(plaintext_bits)  # Length of the key, same as the length of input text in bits
key = generate_key(key_length)  # Generate a random key of the specified length

# Encrypt the plaintext bits using the key
ciphertext_bits = encrypt(plaintext_bits, key)

# Decrypt the ciphertext bits using the same key
decrypted_bits = decrypt(ciphertext_bits, key)

# Convert bits back to text
decrypted_text = bits_to_text(decrypted_bits)

print("Input Text:", plaintext_text)
print("Input Bits:", plaintext_bits)
print("Key:", key)
print("Ciphertext Bits:", ciphertext_bits)
print("Decrypted Bits:", decrypted_bits)
print("Decrypted Text:", decrypted_text)
