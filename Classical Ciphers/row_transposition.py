def generate_row_transposition_table(key):
    # Generate the row transposition table based on the given key
    key_order = [int(i) for i in key]
    num_columns = len(key_order)
    transposition_table = sorted(range(num_columns), key=lambda k: key_order[k])
    return transposition_table

def print_transposition_table(table):
    print("Row Transposition Table:")
    for i, idx in enumerate(table):
        print(f"Column {i + 1} -> Original Column {idx + 1}")

def encrypt(text, key):
    key = [int(i) for i in key]
    num_columns = len(key)
    num_rows = -(-len(text) // num_columns)  # Ceiling division to determine the number of rows
    text = text.ljust(num_rows * num_columns, 'X')  # Pad with 'X' if needed

    # Create an empty matrix to hold the plaintext
    matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]

    # Fill the matrix with the plaintext using row transposition
    transposition_table = generate_row_transposition_table(key)
    for i in range(num_rows):
        for j in range(num_columns):
            matrix[i][j] = text[i * num_columns + transposition_table[j]]
    transposition_table = generate_row_transposition_table(key)
    print_transposition_table(transposition_table)

    # Read the matrix column-wise to create the ciphertext
    ciphertext = ''
    for j in range(num_columns):
        for i in range(num_rows):
            ciphertext += matrix[i][j]

    return ciphertext

def decrypt(ciphertext, key):
    key = [int(i) for i in key]
    num_columns = len(key)
    num_rows = -(-len(ciphertext) // num_columns)  # Ceiling division to determine the number of rows

    # Create an empty matrix to hold the ciphertext
    matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]

    # Fill the matrix with the ciphertext using row transposition
    transposition_table = generate_row_transposition_table(key)
    for j in range(num_columns):
        for i in range(num_rows):
            matrix[i][transposition_table[j]] = ciphertext[j * num_rows + i]

    # Read the matrix row-wise to create the plaintext
    plaintext = ''
    for i in range(num_rows):
        for j in range(num_columns):
            plaintext += matrix[i][j]

    # Remove padding 'X' characters from the decrypted text
    plaintext = plaintext.rstrip('X')
    return plaintext

# Example usage:
plaintext = "thisisrowtranspositionimplementationcode"
key = "3124"  # This key specifies the order in which the rows are read

ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted_text = decrypt(ciphertext, key)
print("Decrypted Text:", decrypted_text)
