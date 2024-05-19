def generate_vigenere_table():
    # Generate the Vigenère table (Vigenère square)
    table = [[chr((i + j) % 26 + ord('A')) for j in range(26)] for i in range(26)]
    return table

def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key_length = len(key)
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            key_char = key[i % key_length]
            key_shift = ord(key_char.upper()) - ord('A')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - key_shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - key_shift) % 26 + ord('a'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Example usage:
def main(): 
    ciphertext =input("Enter the ciphertext: ")
    key = input("Enter the key (Ensure encryption and decryptuon keys are same): ")

    vigenere_table = generate_vigenere_table()
    print("Vigenère Table:")
    for row in vigenere_table:
        print(" ".join(row))

    plaintext = vigenere_decrypt(ciphertext, key)
    print("Decrypted Text:", plaintext)
if __name__ == "__main__":
  main()
