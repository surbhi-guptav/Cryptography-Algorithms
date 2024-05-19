# SHA-256 implementation (without hashlib library)
def sha256(data):
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

    # Initial hash values (first 32 bits of fractional parts of the square roots of the first 8 primes)
    H = [
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
    ]

    # Pre-processing: Padding the message
    data += b'\x80'  # Add a 1 bit followed by zeros
    while len(data) % 64 != 56:
        data += b'\x00'
    data += (8 * len(data)).to_bytes(8, 'big')  # Append the length of the original message

    # Process the message in blocks of 512 bits (64 bytes)
    for i in range(0, len(data), 64):
        chunk = data[i:i + 64]
        w = [0] * 64  # Message schedule (64 words of 32 bits each)

        # Prepare message schedule
        for j in range(16):
            w[j] = int.from_bytes(chunk[j * 4:j * 4 + 4], 'big')
        for j in range(16, 64):
            s0 = (w[j - 15] >> 7 | w[j - 15] << 25) ^ (w[j - 15] >> 18 | w[j - 15] << 14) ^ (w[j - 15] >> 3)
            s1 = (w[j - 2] >> 17 | w[j - 2] << 15) ^ (w[j - 2] >> 19 | w[j - 2] << 13) ^ (w[j - 2] >> 10)
            w[j] = (w[j - 16] + s0 + w[j - 7] + s1) & 0xFFFFFFFF

        # Initialize hash value for this chunk
        a, b, c, d, e, f, g, h = H

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

        # Update hash values for this chunk
        H[0] = (H[0] + a) & 0xFFFFFFFF
        H[1] = (H[1] + b) & 0xFFFFFFFF
        H[2] = (H[2] + c) & 0xFFFFFFFF
        H[3] = (H[3] + d) & 0xFFFFFFFF
        H[4] = (H[4] + e) & 0xFFFFFFFF
        H[5] = (H[5] + f) & 0xFFFFFFFF
        H[6] = (H[6] + g) & 0xFFFFFFFF
        H[7] = (H[7] + h) & 0xFFFFFFFF

    # Convert the hash values to bytes (little-endian)
    hash_bytes = b''
    for h in H:
        hash_bytes += h.to_bytes(4, 'little')

    return hash_bytes

# HMAC-SHA256 function
def hmac_sha256(key, message):
    # Block size and output size for SHA-256
    block_size = 64  # 64 bytes for SHA-256
    output_size = 32  # 32 bytes for SHA-256

    # If the key is longer than block size, hash it
    if len(key) > block_size:
        key = sha256(key)

    # If the key is shorter than block size, pad it with zeros
    if len(key) < block_size:
        key = key.ljust(block_size, b'\x00')

    # XOR key with outer and inner pads
    outer_pad = bytes((x ^ 0x5c) for x in key)
    inner_pad = bytes((x ^ 0x36) for x in key)

    # Calculate inner hash: HMAC(K, text) = H((K ⊕ opad) || H((K ⊕ ipad) || text))
    inner_hash_input = inner_pad + message
    inner_hash = sha256(inner_hash_input)

    # Calculate final HMAC hash
    outer_hash_input = outer_pad + inner_hash
    hmac_digest = sha256(outer_hash_input)

    return hmac_digest

# Secret key and message
secret_key = b'cryptography'
message = b"ThisistheHMACimplementation"

# Calculate HMAC-SHA256
hmac_digest = hmac_sha256(secret_key, message)

# Print the HMAC digest
print("Plaintext : ", message)
print("HMAC Digest (SHA-256):", hmac_digest.hex())
