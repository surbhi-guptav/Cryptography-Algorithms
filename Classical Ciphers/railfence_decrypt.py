def rail_fence_decrypt(ciphertext, rails):
    rail_fence = [['' for _ in range(len(ciphertext))] for _ in range(rails)]

    # Calculate the zigzag pattern
    zigzag = []
    row, direction = 0, 1
    for i in range(len(ciphertext)):
        zigzag.append((row, i))
        row += direction
        if row == rails - 1 or row == 0:
            direction *= -1

    # Fill in the rail fence pattern with 'X' as a placeholder
    for row, col in zigzag:
        rail_fence[row][col] = 'X'

    # Replace 'X' with the characters from the ciphertext
    ciphertext_index = 0
    for i in range(rails):
        for j in range(len(ciphertext)):
            if rail_fence[i][j] == 'X' and ciphertext_index < len(ciphertext):
                rail_fence[i][j] = ciphertext[ciphertext_index]
                ciphertext_index += 1

    # Read the rail fence pattern to create the plaintext
    plaintext = ''
    row, direction = 0, 1
    for j in range(len(ciphertext)):
        plaintext += rail_fence[row][j]
        row += direction
        if row == rails - 1 or row == 0:
            direction *= -1

    return plaintext

# Example usage:
ciphertext = "AeJLcBbonioh"
rails = 3

plaintext = rail_fence_decrypt(ciphertext, rails)
print("Decrypted Text:", plaintext)
