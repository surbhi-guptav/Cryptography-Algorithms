# Function to perform SHA-256 compression
def sha256_compress(block):
    # SHA-256 constants
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
    H = [
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
    ]
    
    # Message schedule (Wt = Sigma1(W(t-2)) + W(t-7) + Sigma0(W(t-15)) + W(t-16))
    W = [0] * 64
    for t in range(16):
        W[t] = (block[t * 4] << 24) | (block[t * 4 + 1] << 16) | (block[t * 4 + 2] << 8) | block[t * 4 + 3]
    for t in range(16, 64):
        W[t] = (W[t - 16] + W[t - 7] + ((W[t - 15] >> 7 | (W[t - 15] << 25)) ^ (W[t - 15] >> 18 | (W[t - 15] << 14)) ^ (W[t - 15] >> 3)) + ((W[t - 2] >> 17 | (W[t - 2] << 15)) ^ (W[t - 2] >> 19 | (W[t - 2] << 13)) ^ (W[t - 2] >> 10))) & 0xFFFFFFFF
    
    # Compression function
    a, b, c, d, e, f, g, h = H
    
    for t in range(64):
        T1 = (h + ((e >> 6 | (e << 26)) ^ (e >> 11 | (e << 21)) ^ (e >> 25 | (e << 7))) + ((e & f) ^ ((~e) & g)) + K[t] + W[t]) & 0xFFFFFFFF
        T2 = (((a >> 2 | (a << 30)) ^ (a >> 13 | (a << 19)) ^ (a >> 22 | (a << 10))) + ((a & b) ^ (a & c) ^ (b & c))) & 0xFFFFFFFF
        h = g
        g = f
        f = e
        e = (d + T1) & 0xFFFFFFFF
        d = c
        c = b
        b = a
        a = (T1 + T2) & 0xFFFFFFFF
    
    # Update hash values
    H[0] = (H[0] + a) & 0xFFFFFFFF
    H[1] = (H[1] + b) & 0xFFFFFFFF
    H[2] = (H[2] + c) & 0xFFFFFFFF
    H[3] = (H[3] + d) & 0xFFFFFFFF
    H[4] = (H[4] + e) & 0xFFFFFFFF
    H[5] = (H[5] + f) & 0xFFFFFFFF
    H[6] = (H[6] + g) & 0xFFFFFFFF
    H[7] = (H[7] + h) & 0xFFFFFFFF
    
    # Return the hash values (as bytes)
    hash_bytes = b''
    for value in H:
        hash_bytes += value.to_bytes(4, byteorder='big')
    
    return hash_bytes

# HMAC function without hashlib
def hmac_sha256(key, message):
    block_size = 64  # Block size for SHA-256 (in bytes)
    
    # If the key is longer than block size, hash it
    if len(key) > block_size:
        key = sha256_compress(key)
    
    # If the key is shorter than block size, pad it with zeros
    if len(key) < block_size:
        key = key.ljust(block_size, b'\x00')
    
    # XOR key with outer and inner pads
    outer_pad = bytes((x ^ 0x5c) for x in key)
    inner_pad = bytes((x ^ 0x36) for x in key)
    
    # Calculate inner hash: HMAC(K, text) = H((K ⊕ opad) || H((K ⊕ ipad) || text))
    inner_hash_input = inner_pad + message.encode('utf-8')
    inner_hash = sha256_compress(inner_hash_input)
    
    # Calculate final HMAC hash
    outer_hash_input = outer_pad + inner_hash
    hmac_digest = sha256_compress(outer_hash_input)
    
    return hmac_digest

# Example usage
secret_key = b'Hemrajsir'
message = 'thisisMACcodeimplementation'

# Generate HMAC
generated_hmac = hmac_sha256(secret_key, message)

# Received HMAC (simulating received HMAC)
received_hmac = generated_hmac
generated_hmac_hex = generated_hmac.hex()
print("plaintext : ",message)
print("Generated HMAC (Hex):", generated_hmac_hex)

# Verify HMAC
if received_hmac == generated_hmac:
    print("HMAC is valid. Message is authentic and has not been tampered with.")
else:
    print("HMAC is not valid. Message may have been tampered with.")
