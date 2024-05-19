def generate_vigenere_table():
    # Generate the Vigenère table (Vigenère square)
    table = [[chr((i + j) % 26 + ord('A')) for j in range(26)] for i in range(26)]
    return table

def vigenere_encrypt(plaintext, key):
    encrypted_text = ""
    key_length = len(key)
    vigenere_table = generate_vigenere_table()

    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            key_char = key[i % key_length].upper()
            row_index = ord(key_char) - ord('A')
            if char.isupper():
                encrypted_char = vigenere_table[row_index][ord(char) - ord('A')]
            else:
                encrypted_char = vigenere_table[row_index][ord(char) - ord('a')]

            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def main():
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the key: ")

    vigenere_table = generate_vigenere_table()
    print("Vigenère Table:")
    for row in vigenere_table:
        print(" ".join(row))

    ciphertext = vigenere_encrypt(plaintext, key)
    print("Ciphertext:", ciphertext)

if __name__ == "__main__":
    main()
