def rail_fence_encrypt(plain_text, rails):
    rail_fence = [['' for _ in range(len(plain_text))] for _ in range(rails)]

    # Fill in the rail fence pattern with the plaintext
    row, direction = 0, 1
    for char in plain_text:
        rail_fence[row] += char
        row += direction

        if row == rails - 1 or row == 0:
            direction *= -1

    # Read the rail fence pattern to create the ciphertext
    ciphertext = ''.join(''.join(row) for row in rail_fence)
    return ciphertext

# Example usage:
plaintext = "ALiceBobJohn"
rails = 3
print("plaintext: ",plaintext)
ciphertext = rail_fence_encrypt(plaintext, rails)
print("Ciphertext:", ciphertext)
