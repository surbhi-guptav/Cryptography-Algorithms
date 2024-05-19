# Data to be combined
data1 = "combined "
data2 = "hash "
data3 = "code"

# Combine the data
combined_data = data1 + data2 + data3

# Custom SHA-256 hash function
def custom_sha256(data):
    # Constants for SHA-256
    K = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]

    # Initial hash values (first 32 bits of the fractional parts of the square roots of the first 8 primes)
    h0, h1, h2, h3, h4, h5, h6, h7 = 0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19

    # Pre-processing: Padding the message
    data_bytes = data.encode()
    ml = len(data_bytes) * 8  # Message length in bits
    data_bytes += b'\x80'  # Padding with a single '1' bit
    data_bytes += b'\x00' * ((56 - len(data_bytes) % 64) % 64)  # Padding with '0' bits
    data_bytes += ml.to_bytes(8, byteorder='big')  # 64-bit representation of the original message length

    # Process the message in blocks of 512 bits (64 bytes)
    for i in range(0, len(data_bytes), 64):
        block = data_bytes[i:i + 64]

        # Break the block into 16 32-bit big-endian words
        w = [int.from_bytes(block[j:j + 4], byteorder='big') for j in range(0, 64, 4)]

        # Extend the 16 words into 64 words
        for j in range(16, 64):
            s0 = (w[j - 15] >> 7 | w[j - 15] << 25) ^ (w[j - 15] >> 18 | w[j - 15] << 14) ^ (w[j - 15] >> 3)
            s1 = (w[j - 2] >> 17 | w[j - 2] << 15) ^ (w[j - 2] >> 19 | w[j - 2] << 13) ^ (w[j - 2] >> 10)
            w.append((w[j - 16] + s0 + w[j - 7] + s1) & 0xFFFFFFFF)

        # Initialize hash values for this chunk
        a, b, c, d, e, f, g, h = h0, h1, h2, h3, h4, h5, h6, h7

        # Main loop
        for j in range(64):
            S1 = (e >> 6 | e << 26) ^ (e >> 11 | e << 21) ^ (e >> 25 | e << 7)
            ch = (e & f) ^ (~e & g)
            temp1 = h + S1 + ch + K[j] + w[j]
            S0 = (a >> 2 | a << 30) ^ (a >> 13 | a << 19) ^ (a >> 22 | a << 10)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = S0 + maj

            h = g
            g = f
            f = e
            e = (d + temp1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xFFFFFFFF

        # Update hash values
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF
        h5 = (h5 + f) & 0xFFFFFFFF
        h6 = (h6 + g) & 0xFFFFFFFF
        h7 = (h7 + h) & 0xFFFFFFFF

    # Final hash value (concatenation of hash segments)
    hash_result = h0.to_bytes(4, byteorder='big') + h1.to_bytes(4, byteorder='big') + h2.to_bytes(4, byteorder='big') + h3.to_bytes(4, byteorder='big') + h4.to_bytes(4, byteorder='big') + h5.to_bytes(4, byteorder='big') + h6.to_bytes(4, byteorder='big') + h7.to_bytes(4, byteorder='big')
    return hash_result

# Create a hash of the combined data
hash_combined = custom_sha256(combined_data)

# Print the combined data and its hash
print(f"Combined Data: {combined_data}")
print(f"Combined Hash (SHA-256): {hash_combined.hex()}")
