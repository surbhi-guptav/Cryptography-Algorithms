# Custom AES encryption using CBC mode
import os 
def aes_encrypt_cbc(data, key, iv):
    def xor_bytes(b1, b2):
        return bytes(x ^ y for x, y in zip(b1, b2))

    # Padding the data to be multiple of 16 bytes (AES block size)
    padded_data = data + b'\x10' * (16 - len(data) % 16)
    ciphertext = b""
    prev_block = iv
    
    for i in range(0, len(padded_data), 16):
        block = padded_data[i:i + 16]
        xor_block = xor_bytes(block, prev_block)
        encrypted_block = xor_block  # Custom encryption logic (replace this with proper AES implementation)
        ciphertext += encrypted_block
        prev_block = encrypted_block
    
    return ciphertext

# Custom AES decryption using CBC mode
def aes_decrypt_cbc(ciphertext, key, iv):
    def xor_bytes(b1, b2):
        return bytes(x ^ y for x, y in zip(b1, b2))
    
    decrypted_data = b""
    prev_block = iv
    
    for i in range(0, len(ciphertext), 16):
        block = ciphertext[i:i + 16]
        decrypted_block = xor_bytes(block, prev_block)
        decrypted_data += decrypted_block
        prev_block = block
    
    # Remove padding to get the original data
    unpadded_data = decrypted_data.rstrip(b'\x10')
    return unpadded_data
def calculate_avalanche_effect(input_data, altered_data, key, iv):
    ciphertext1 = aes_encrypt_cbc(input_data, key, iv)
    ciphertext2 = aes_encrypt_cbc(altered_data, key, iv)
    differences = sum([bit1 != bit2 for bit1, bit2 in zip(ciphertext1, ciphertext2)])
    total_bits = len(ciphertext1) * 8  # Total number of bits
    percentage_difference = (differences / total_bits) * 100
    
    return percentage_difference
    return differences

# Example usage (generating key and IV)
key = os.urandom(16)  # 128-bit key
iv = os.urandom(16)   # 128-bit IV
data = b"Surbhi Piyush Roshni "

ciphertext = aes_encrypt_cbc(data, key, iv)
print("Ciphertext (Base64 representation):", ciphertext.hex())

decrypted_data = aes_decrypt_cbc(ciphertext, key, iv)
print("Decrypted Data (ASCII representation):", decrypted_data.decode('utf-8'))

# Alter the input data slightly
altered_data = b"This is CBC mode implementation"

# Calculate avalanche effect
avalanche_effect = calculate_avalanche_effect(data, altered_data, key, iv)

print("Avalanche Effect (Number of different bits between ciphertexts):", avalanche_effect)
