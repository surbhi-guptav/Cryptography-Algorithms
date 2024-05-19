import string
import time

def generate_matrix(keyword):
    """
    Generates a Polybius square matrix based on a keyword.

    Args:
    - keyword: A string representing the keyword.

    Returns:
    - A 6x6 matrix representing the Polybius square.
    """
    keyword = ''.join(sorted(set(keyword.upper()), key=lambda x: keyword.upper().index(x)))
    square = [['' for _ in range(6)] for _ in range(6)]
    alphabet = keyword + ''.join([c for c in string.ascii_uppercase if c not in keyword])
    row, col = 0, 0
    for char in alphabet:
        square[row][col] = char
        col += 1
        if col == 6:
            col = 0
            row += 1
    return square

def encrypt_adfgvx(plaintext, polybius_square, key):
    """
    Encrypts plaintext using the ADFGVX cipher.

    Args:
    - plaintext: The plaintext string to be encrypted.
    - polybius_square: The Polybius square matrix.
    - key: The key for inserting digits into the ciphertext.

    Returns:
    - The encrypted ciphertext.
    """
    plaintext = plaintext.upper()
    cipher_text = ''
    letter_to_code = {}
    for row in range(6):
        for col in range(6):
            letter = polybius_square[row][col]
            code = 'ADFGVX'[row] + 'ADFGVX'[col]
            letter_to_code[letter] = code
    # Encrypt the plaintext
    for char in plaintext:
        if char in letter_to_code:
            cipher_text += letter_to_code[char]

    key_mapping = {}
    digit = 1
    for char in key:
        if char not in key_mapping and char.isalpha():
            key_mapping[char] = str(digit)
            digit += 1

    for key_char, digit in key_mapping.items():
        cipher_text = cipher_text.replace(key_char, digit)

    return cipher_text

def decrypt_adfgvx(ciphertext, polybius_square, key):
    """
    Decrypts ciphertext encrypted using the ADFGVX cipher.

    Args:
    - ciphertext: The ciphertext string to be decrypted.
    - polybius_square: The Polybius square matrix.
    - key: The key used for inserting digits into the ciphertext.

    Returns:
    - The decrypted plaintext.
    """
    key_mapping = {}
    digit = 1
    for char in key:
        if char not in key_mapping and char.isalpha():
            key_mapping[char] = str(digit)
            digit += 1

    # Reverse the digit substitution
    for key_char, digit in key_mapping.items():
        ciphertext = ciphertext.replace(digit, key_char)

    # Reverse the ADFGVX encryption
    letter_to_code = {}
    for row in range(6):
        for col in range(6):
            letter = polybius_square[row][col]
            code = 'ADFGVX'[row] + 'ADFGVX'[col]
            letter_to_code[code] = letter

    plaintext = ''
    i = 0
    while i < len(ciphertext):
        code = ciphertext[i:i+2]
        if code in letter_to_code:
            plaintext += letter_to_code[code]
        i += 2

    return plaintext

def reorder_columns(ciphertext, key):
    """
    Reorders columns of the ciphertext based on the provided key.

    Args:
    - ciphertext: The ciphertext string to be reordered.
    - key: The key used for reordering columns.

    Returns:
    - The ciphertext with reordered columns.
    """
    original_order = list(key)
    sorted_order = sorted(original_order)
    num_columns = len(key)

    num_rows = len(ciphertext) // num_columns
    if len(ciphertext) % num_columns != 0:
        num_rows += 1

    columns = [['' for _ in range(num_rows)] for _ in range(num_columns)]

    for i, char in enumerate(ciphertext):
        col = sorted_order.index(key[i % num_columns])
        row = i // num_columns
        columns[col][row] = char

    final_ciphertext = ''.join([''.join(column) for column in columns])

    return final_ciphertext

# Define the codeword for generating the Polybius square
codeword = "nachtbommmenwerper"

# Generate the Polybius square
polybius_square = generate_matrix(codeword)

# Input plaintext to be encrypted
plaintext = input("Enter the plain text:  ")

# Define the key for inserting digits
key = input("Enter the key: ")

# Encrypt the plaintext
start_time = time.time()
cipher_text = encrypt_adfgvx(plaintext, polybius_square, key)
end_time = time.time()
encryption_time = end_time - start_time

# Decrypt the ciphertext
start_time = time.time()
decrypted_text = decrypt_adfgvx(cipher_text, polybius_square, key)
end_time = time.time()
decryption_time = end_time - start_time

# Reorder the columns of the ciphertext
final_ciphertext = reorder_columns(cipher_text, key)

# Display the Polybius square and the resulting ciphertext
print("Polybius Square:")
for row in polybius_square:
    print(' '.join(row))

print("Ciphertext:", final_ciphertext)
print("Encryption Time:", encryption_time, "seconds")
print("Decrypted Text:", decrypted_text)
print("Decryption Time:", decryption_time, "seconds")
