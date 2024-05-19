# XOR operation for bytes
import os


def xor_bytes(b1, b2):
    return bytes(x ^ y for x, y in zip(b1, b2))

# Key derivation function to derive a secure encryption key from a password
def derive_key(password, salt):
    key = b""
    for i in range(len(password)):
        key += bytes([password[i] ^ salt[i % len(salt)]])
    return key

# Encrypt data using CFB mode
def encrypt_cfb(data, key, iv):
    encrypted_data = b""
    prev_block = iv

    for i in range(len(data)):
        keystream = xor_bytes(prev_block, key)
        cipher_byte = data[i] ^ keystream[0]
        encrypted_data += bytes([cipher_byte])
        prev_block = prev_block[1:] + bytes([cipher_byte])

    return encrypted_data

# Decrypt data using CFB mode
def decrypt_cfb(ciphertext, key, iv):
    decrypted_data = b""
    prev_block = iv

    for i in range(len(ciphertext)):
        keystream = xor_bytes(prev_block, key)
        decrypted_byte = ciphertext[i] ^ keystream[0]
        decrypted_data += bytes([decrypted_byte])
        prev_block = prev_block[1:] + bytes([ciphertext[i]])

    return decrypted_data
def bytes_to_hex_string(byte_array):
    return ''.join(format(byte, '02x') for byte in byte_array)

# Example usage
password = b"mysecretpassword"
data = b"this is CFB mode implementation"

salt = os.urandom(16)  # Generate a random salt
key = derive_key(password, salt)
iv = os.urandom(16)    # Initialization Vector (IV)

ciphertext = encrypt_cfb(data, key, iv)
ciphertext_hex = bytes_to_hex_string(ciphertext)
print("Ciphertext (Hexadecimal representation):", ciphertext_hex)

decrypted_data = decrypt_cfb(ciphertext, key, iv)
print("Decrypted Data :", decrypted_data)
