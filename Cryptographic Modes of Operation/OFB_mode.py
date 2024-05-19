# Define your own block cipher function (for example, a simple XOR function)

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


# OFB encryption function

def ofb_encrypt(plaintext, key, iv):
    ciphertext = b""
    block_size = len(key)  
    # Block size is determined by the key size

    for i in range(0, len(plaintext), block_size):
        # Generate the keystream block by encrypting the IV with the key
        keystream_block = xor_bytes(iv, key)
        ciphertext_block = xor_bytes(plaintext[i:i + block_size], keystream_block)
        ciphertext += ciphertext_block

        # Update IV for the next iteration
        iv = keystream_block

    return ciphertext

# OFB decryption function (same as encryption)

def ofb_decrypt(ciphertext, key, iv):
    return ofb_encrypt(ciphertext, key, iv)

# Example usage

key = b'cryptography'  # 8 bytes key for DES, adjust if using different cipher
iv = b'InitializationVector'  # Should be the same length as the key

plaintext = b'thisisOFBmodeimplementation'
encrypted_text = ofb_encrypt(plaintext, key, iv)
decrypted_text = ofb_decrypt(encrypted_text, key, iv)

print("Plaintext:", plaintext)
# Encode encrypted text in base64
base64_output = ""
for char in encrypted_text:
    base64_output += format(char, '02x')  # Convert to hexadecimal
print("Encrypted text (hexadecimal):", base64_output)
print("Decrypted Text:", decrypted_text)
